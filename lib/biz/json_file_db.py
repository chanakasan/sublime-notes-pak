import json

class JsonFileDb:
  def __init__(self, db_file, model_key):
    self.db_file = db_file
    self.model_key = model_key
    
  def db_path(self):
    filename = self.db_file + '.json'
    base = "C:/Local/app_data/sublime_mods/"
    file = base + filename
    return file
  
  def model_name(self):
    return self.model_key
  
  def _clear_data(self):
    data = {}
    self.set_list(data, {})
    self._write_json_data(data)
    
  def _write_json_data(self, data):
      db_file = self.db_path()
      with open(db_file, 'w') as outfile:
          json.dump(data, outfile)
         
  def _read_json_data(self):
    db_file = self.db_path()
    with open(db_file) as json_file:
        data = json.load(json_file)
    return data

  def get_all(self):
    data = self._read_json_data()
    list = data[self.model_name()]
    return list
      
  def get_one(self, name):
    data = self._read_json_data()
    list = self.get_list(data)
    if (name in list):
        return list[name]
    raise ValueError('Proj not found: ' + name)
    
  def add_one(self, name):
    data = self._read_json_data()
    list = self.get_list(data)
    list[name] = "1"
    self.set_list(data, list)
    self._write_json_data(data)
    return True

  def update_one(self, name, new_name):
    data = self._read_json_data()
    list = self.get_list(data)
    if (name in list):
      list.pop(name)
    list[new_name] = "1"
    self.set_list(data, list)
    self._write_json_data(data)
      
  def delete_one(self, name):
    data = self._read_json_data()
    list = self.get_list(data)
    if (name in list):
      list.pop(name)
    self.set_list(data, list)
    self._write_json_data(data)
    return True
    
  def set_list(self, data, list):
    data[self.model_name()] = list
  
  def get_list(self, data):
    list = data[self.model_name()]
    return list