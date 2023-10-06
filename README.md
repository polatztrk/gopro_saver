# gopro_saver

This Python script is designed to organize and rename GoPro video files. It scans multiple paths on removable media for GoPro video files, renames them with a timestamp and camera ID, and copies them to a destination directory.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
  
## Introduction

GoPro cameras typically generate video files with non-descriptive filenames. This script helps you organize and rename those files for easier management. It detects GoPro video files from specified paths, renames them with timestamps and a camera ID, and then copies them to a destination directory.

## Usage

To use this script:

1. Make sure you have Python installed on your system.

2. Clone or download this repository to your computer.

3. Open a terminal and navigate to the directory where you have saved the script.

4. Run the script using the following command:

   python cameraSaver.py

5. Follow the prompts to select the appropriate device (camera ID) and confirm your choices.

6. The script will search for GoPro video files in the specified paths, rename them, and copy them to the destination directory.

7. Once the process is complete, you'll see a message indicating that all files have been renamed and copied.

## Configuration

You can customize the behavior of the script by modifying the following variables:

- `paths_to_try`: List of paths to search for GoPro video files.
- `dest_filepath`: The destination directory where renamed files will be copied.

Make sure to update these variables according to your specific directory structure and preferences.

## Contributing

Contributions to this script are welcome. If you have improvements, bug fixes, or additional features to add, please feel free to open an issue or create a pull request.




