import os
import argparse
import json
from my_funcs import *

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Cluster audio files in a folder.")
    parser.add_argument("--folder_path", required=True, help="Path to the target folder containing audio files.")
    args = parser.parse_args()

    # Check if the folder path exists
    if not os.path.exists(args.folder_path):
        print(f"Folder path '{args.folder_path}' does not exist.")
        return

    # Cluster the audio files
    cluster_result = cluster_audio_files(args.folder_path)

    # Output the clusters as JSON
    with open("clusters.json", "w") as json_file:
        json.dump(cluster_result, json_file, indent=4)

    print("Clusters saved to 'clusters.json'.")

if __name__ == "__main__":
    main()
