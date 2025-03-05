
def create_new_notebook(name):
  old_name = 'new space ##.sublime-workspace'
  new_name = name + '.sublime-workspace'
  src_path = notes_base_path() + "/root/" + old_name
  new_path = notes_base_path() + "/notepads/" + new_name
  copy_file_safely(src_path, new_path)
  return new_path
