import json
from nex_lib.utils.files import read_file

def read_json_file(file_path, key=False):
  try:
    str = read_file(file_path)
    data = json.loads(str)
    if (key):
      return data[key]
    return data
  except:
    print('************ ERROR *******************')
    print('Error parsing file: '+file_path)
    return []