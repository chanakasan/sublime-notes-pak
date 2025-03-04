import sublime, sublime_plugin
from .helpers import *
from .input_handler import NxProjInputHandler

class NxOpenNotesCommand(sublime_plugin.WindowCommand):
    def run(self, item_name):
        print('')
        print('---' * 10)
        print('NxOpenNotesCommandww')
        print('item_name = ', item_name)
        if (item_name == False):
            print("aborting...")
            return
        self.handle_selected_item(item_name)

    def input(self, args):
        return NxProjInputHandler()
    
    def handle_selected_item(self, item_name):
      if "new ##" in item_name:
          show_input_panel(self.window, self.handle_new_file)
      else:
          ws_path = get_ws_path_from_name(item_name)
          open_sublime_workspace(self.window, ws_path)
          
    def handle_new_file(self, new_name):
        ws_path = create_new_notebook(new_name)
        open_sublime_workspace(self.window, ws_path)

