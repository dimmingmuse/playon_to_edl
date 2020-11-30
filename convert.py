# converts output from FFMPEG to EDL text format
import sys
import requests

chapters_found = False

start_position = 0
end_position = 0
title = ""

for line in sys.stdin:
        if ( line.find("[CHAPTER]") > -1 ):
            chapters_found = True


        if (chapters_found):
            # if ( line.find("[CHAPTER]") == -1 and line.find("TIMEBASE=1/1000")== -1 ):
            if ( line.find("START=") != -1):
                junk,start_position = line.split("START=")
                start_position = int(start_position)/1000
                start_position = str(start_position)
                # print("start="+str(start_position))
            if ( line.find("END=") != -1):
                junk,end_position = line.split("END=")
                end_position = int(end_position)/1000
                end_position = str(end_position)
                # print("end="+str(end_position))
            if ( line.find("title=") != -1):
                junk,title = line.split("title=")
                title = title.strip()
                if (title == "Advertisement"):
                    edl_type = "3"
                    print(start_position+"\t"+end_position+"\t"+edl_type)
