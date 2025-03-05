import os
import sys

def append_sys_path_with(file_path):
  sys.path.append(os.path.dirname(os.path.abspath(file_path)))

append_sys_path_with(__file__)


from app.command import NxOpenNotesCommand
from app.input_handler import NxProjInputHandler
