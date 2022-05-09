from students import StudentDB
import pytest

def test_Peter_data():
    db = StudentDB()
    db.connect('studentsDB.json')
    peter_data = db.get_data('Peter')
    assert peter_data['id'] == 1
    assert peter_data['name'] == 'Peter'
    assert peter_data['lastname'] == 'Stevenson'
    assert peter_data['grade'] == 5

def test_Jake_data():
    db = StudentDB()
    db.connect('studentsDB.json')
    peter_data = db.get_data('Jake')
    assert peter_data['id'] == 2
    assert peter_data['name'] == 'Jake'
    assert peter_data['lastname'] == 'Jackson'
    assert peter_data['grade'] == 4
