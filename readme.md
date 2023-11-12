# About The Project


## Audio - Three voice clustering

This project solves the following problem: there are 9 audio files, each associated with one of three people. I will write a script that will automatically cluster these audio files into clusters according to their respective voices.

#### Deliverable:
* Working Code: Create a functional Python script that can be executed with the "--folder_path" argument followed by the path to the target folder. The script should then output the result clusters in a JSON format. The JSON should contain a dictionary where the keys represent voice IDs, and the values are lists of filenames of audio files belonging to each cluster. For instance:
{ "1": ["1.wav", "2.wav", "3.wav"], "2": ["4.wav", "5.wav", "6.wav"], "3": ["7.wav", "8.wav", "9.wav"] }
* JSON File with Results: JSON file containing the results of your clustering process for the given folder with audio files.

## Navigate

* <b>main.py</b> - This file forms the result in the folder <b>results.json</b>.
* <b>short_report.ipynb</b> - report that explains the underlying principles of my solution.

### Usage

* To create file with results execute this command:
   ```sh
   python main.py --folder_path your_path
   ```

## My talk

I managed to solve this problem, but I want to note a few disadvantages of my project. First, I don't know if it will work on other data. Also, in my opinion, I still have not enough experience, and because of this, perhaps the project has not the best or optimal solution. But I want to say that this project gave me some experience and understanding of how to develop further.
