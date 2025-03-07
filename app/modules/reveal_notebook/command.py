import sublime
import sublime_plugin
import subprocess

class NxRevealNotebookCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        window = sublime.active_window()
        if not window:
            sublime.error_message("No active window found.")
            return
        
        workspace_file = window.workspace_file_name()
        if not workspace_file:
            sublime.error_message("No workspace is currently open.")
            return
        
        # folder = os.path.dirname(workspace_file)
        print(f"current workspace file = {workspace_file}")
        # print(f"current workspace folder = {folder}")
        self.reveal_in_explorer(workspace_file)

    def reveal_in_explorer(self, filepath):
      print(f"revealing file in explorer: {filepath}")
      subprocess.Popen(["explorer.exe", "/select,", filepath])
