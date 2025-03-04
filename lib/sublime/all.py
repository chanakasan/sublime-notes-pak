import sublime
import os, sys

def alert(value):
  sublime.message_dialog(str(value))
  
def append_sys_path_with(file_path):
  sys.path.append(os.path.dirname(os.path.abspath(file_path)))
  
def array_slice(xs, n):
    n = max(1, n)
    return list(xs[i:i+n] for i in range(0, len(xs), n))
  
def get_dir_basename(dirname):
  return os.path.basename(dirname)

def dirname(file_path):
  str = os.path.dirname(os.path.realpath(file_path))
  return str.replace("\\", "/")
