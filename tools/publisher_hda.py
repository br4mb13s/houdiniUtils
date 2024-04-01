import os
import hou
import sys

#Houdini HDA script for Publishing bgeo cache

class Publisher:
    def publish():
        
        hou.pwd().parm("file").set("$HIP/geo/$HIPNAME.$OS.$F.bgeo.sc")
        default_path = hou.pwd().parm("file").evalAsString()

        #Save location derived from user environment variable
        dest_path = "G:/My Drive/dev/production_assets"

        try:
            file_version = len([file for file in os.listdir(dest_path) if file.endswith("bgeo.sc")])+1
        except:
            os.mkdir(dest_path)
            file_version = len([file for file in os.listdir(dest_path) if file.endswith("bgeo.sc")])+1
        print("Setting file version: ", file_version)

        _new_file_path = f"{dest_path}/$HIPNAME.$USER_ID.asset_v{file_version}.bgeo.sc"
        hou.pwd().parm("file").set(_new_file_path)