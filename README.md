# NOTICE: this project is not associated with the official Playon nor Playlater applications.  They will not give support for this project.

# playon_to_edl
Utility to use playlater mp4 file to add an edl file for Kodi to skip commercials.  

This project uses ffmpeg and python to create an EDL file so that kodi can skip ads.



# Installation in Linux

* Please be sure that you have ffmpeg and python 3 installed before you begin.

* Copy the files in this repository into your home directory.  Otherwise, you will need to modify to match your choice of installation directory.

# Usage in Linux

* copy files to the Linux system 

* Use the "find" command to find all files to create the EDL files for.  For example:

find ~/playon_files/ -type f -name '*.mp4' -exec ~/convert.sh {} \\;

* You will need to modify this command to reflect the real location of your mp4 files.






