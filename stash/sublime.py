
def show_input_panel(window, on_done):
  window.show_input_panel("New Space Name:", "", on_done, None, None)

def open_sublime_workspace(window, ws_file):
  if not os.path.isfile(ws_file):
    raise ValueError('Invalid file: ' + ws_file)
  # current_workspace_path(window)
  window.run_command('close_workspace')
  window.run_command('open_project_or_workspace', {
      'file': ws_file,
  })

def get_current_workspace_path(window):
  # value = window.project_file_name()
  value = window.workspace_file_name()
  alert(value)
