import sublime_plugin
from .helpers import get_nested_proj_list

class NxProjInputHandler(sublime_plugin.ListInputHandler):
    def name(self):
      return 'item_name'
      
    def list_items(self):
        return sorted(get_nested_proj_list())
