from lib.sublime.debug import alert

def current_workspace_path(window):
  # value = window.project_file_name()
  value = window.workspace_file_name()
  alert(value)
