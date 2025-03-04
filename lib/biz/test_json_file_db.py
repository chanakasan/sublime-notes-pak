from nex_lib.json_file_db import JsonFileDb
import pytest

class TestJsonFileDb:
  def reset_db(self):
    service = self.service
    service._clear_data()
    service.add_one("one")
    service.add_one("two")
    service.add_one("three")
  
  @pytest.fixture(autouse=True)
  def run_around_tests(self):
    self.service = JsonFileDb('proj', 'projects')
    self.reset_db()
    result = self.service.get_all()
    expected = {"one": "1", "two": "1", "three": "1"}
    assert expected == result
    yield
      
  def test_add(self):
    service = self.service
    result = service.add_one("four")
    result = service.get_all()
    expected = {"four": "1", "one": "1", "two": "1", "three": "1"}
    assert expected == result

  def test_remove(self):
    service = self.service
    service.delete_one("two")
    result = service.get_all()
    expected = {"one": "1", "three": "1"}
    assert expected == result

  def test_update(self):
    service = self.service
    service.update_one("two", "two-plus")
    result = service.get_all()
    expected = {"one": "1", "two-plus": "1", "three": "1"}
    assert expected == result

  def test_get_one(self):
    service = self.service
    service.add_one("one")
    service.add_one("two")
    service.add_one("three")
    result = service.get_one("two")
    expected = "1"
    assert expected == result
