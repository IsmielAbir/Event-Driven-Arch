import glob
import shutil
import os

source_path = '../source/*'

source_object = glob.glob(source_path)
#print(source_object)

object_path = source_object[0]
shutil.copy(object_path, '.')