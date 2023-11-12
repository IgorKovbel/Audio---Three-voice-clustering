import os
import librosa
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import json

def extract_features(audio_file):
    # Extract features from an audio file (MFCC, F0)
    y, sr = librosa.load(audio_file)
    
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    
    # Extract F0 (fundamental frequency)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    f0 = []
    for i in range(pitches.shape[1]):
        f0_frame = pitches[:, i]
        if np.any(f0_frame > 0):  # Check if there is at least one F0 value > 0
            f0_value = f0_frame[f0_frame > 0][0]
            f0.append(f0_value)

    # Make both arrays of the same length by padding the shorter array with zeros
    max_length = max(mfcc.shape[1], len(f0))
    mfcc = np.pad(mfcc, ((0, 0), (0, max_length - mfcc.shape[1])), mode='constant')
    f0 = np.pad(f0, (0, max_length - len(f0)), mode='constant')

    # Concatenate all features together
    features = np.vstack((mfcc, f0))
    
    return features.mean(axis=1)


def cluster_audio_files(folder_path):
    # Get a list of audio files in the specified folder
    audio_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.wav')]

    # Extract features from each audio file
    features = [extract_features(file) for file in audio_files]

    # Normalize acoustic features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Use K-Means for voice clustering
    num_clusters = 3  # Change this to a higher number if needed
    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(features_scaled)

    # Create a dictionary where keys are cluster IDs (converted to str), and values are files belonging to each cluster
    result = {}
    for i, cluster_id in enumerate(clusters):
        audio_file = os.path.basename(audio_files[i])
        str_cluster_id = str(cluster_id)  # Convert the key to str
        if str_cluster_id not in result:
            result[str_cluster_id] = [audio_file]
        else:
            result[str_cluster_id].append(audio_file)

    return result

if __name__ == "__main__":
    folder_path = "Audio - Three voice clustering"
    clusters = cluster_audio_files(folder_path)
    print(folder_path)

    # Save the results to a JSON file
    with open("results.json", "w") as json_file:
        json.dump(clusters, json_file, indent=4)
