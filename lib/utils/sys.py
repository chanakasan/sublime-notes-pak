import os, sys

def append_sys_path_with(file_path):
  sys.path.append(os.path.dirname(os.path.abspath(file_path)))