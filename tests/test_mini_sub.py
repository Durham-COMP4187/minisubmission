from minisubmission import *


def test_can_create_class():
    String()


def test_class_has_correct_type():
    obj = String()
    assert obj.type() == str


def test_class_has_correct_name():
    obj = String()
    assert obj.name == "string"
