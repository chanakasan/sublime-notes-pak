import os

def get_dir_path(base_path, start):
  return base_path + "/" + start

def get_nested_files_list(base_path, start=""):
  result = []
  source = get_dir_path(base_path, start)
  items = os.listdir(source)
  for i,val in enumerate(items):
    if (os.path.isdir(get_dir_path(base_path, val))):
      sub_list = get_nested_files_list(base_path, val)
      result += sub_list
    else:
      prefix = "" if start == "" else start + " > "
      result.append(prefix + val)     
  return result

def get_files_list(path, suffix=False, cb=False):
  files = os.listdir(path)
  if suffix:
    files = filter(lambda x: x.endswith(suffix), files)
  if cb:
    return map(cb, files)
  return files

def get_dir_list(path):
  result = os.listdir(path)
  list = filter(lambda x: os.path.isdir(os.path.join(path, x)), result)
  return list

def read_file(file_path):
  content = ""
  with open(file_path, 'r') as f:
    content = f.read()
  return content

def get_dir_basename(dirname):
  return os.path.basename(dirname)

def dirname(file_path):
  str = os.path.dirname(os.path.realpath(file_path))
  return str.replace("\\", "/")