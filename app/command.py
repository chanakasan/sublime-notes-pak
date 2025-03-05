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
        ws_path = get_ws_path_from_name(item_name)
        open_sublime_workspace(self.window, ws_path)
