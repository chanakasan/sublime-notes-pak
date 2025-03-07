import os
import sys

def append_sys_path_with(file_path):
  sys.path.append(os.path.dirname(os.path.abspath(file_path)))

append_sys_path_with(__file__)

from app.modules.open_notebook.command import NxOpenNotebookCommand
from app.modules.reveal_notebook.command import NxRevealNotebookCommand
