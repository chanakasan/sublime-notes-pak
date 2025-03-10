from app.utils import current_workspace_path
from app.config import notes_base_path
from lib.utils.files import *
from lib.sublime.debug import *
import shutil

def get_proj_list():
  base_path = notes_base_path()
  suffix = ".sublime-workspace"
  cb = lambda x: x.split(suffix, 1)[0]
  return list(get_files_list(base_path, suffix, cb))

def get_nested_proj_list(start=""):    
  suffix = ".sublime-workspace"
  result = get_nested_files_list(notes_base_path())
  # filter by extension
  result = filter(lambda x: x.endswith(suffix), result)
  # remove extension
  result = map(lambda x: x.split(suffix, 1)[0], result)
  # Push "new#" to the result list
  result = list(result)  # Convert map object to list
  result.append("new##")
  return result

def get_ws_path_from_name(name):
  parts = name.split('>')
  path = notes_base_path()
  for s in parts:
    path += '/' + s.strip()
  return path + '.sublime-workspace'

def copy_file_safely(src_path, dest_path):
  if os.path.isfile(dest_path):
    raise "Copy Error: file exists"
  if not os.path.isfile(dest_path):
    shutil.copyfile(src_path, dest_path)

def open_sublime_workspace(window, ws_file):
  if not os.path.isfile(ws_file):
    raise ValueError('Invalid file: ' + ws_file)
  window.run_command('close_workspace')
  window.run_command('open_project_or_workspace', {
      'file': ws_file,
  })
