import pytest
from todo import add, remove, change, ToDoList, todo_list, titles

def test_add():
    first = add("title, 1, type, details")
    second = ToDoList("title", 1, "type", "details")
    assert first.title == second.title
    assert first.priority == second.priority
    assert first.type == second.type
    assert first.details == second.details
    name_errors = ["title, 1, type, ", "title", "title, 11, type, details"]
    for item in name_errors:
        with pytest.raises(NameError):
            add(item)


def test_remove():
    todo_list.append(ToDoList("title", 1, "type", "details"))
    todo_list.append(ToDoList("title2", 2, "type2", "details2"))
    todo_list.append(ToDoList("title3", 3, "type3", "details3"))
    titles.append("title")
    titles.append("title2")
    titles.append("title3")
    assert remove("title") == 0
    assert remove("TITLE2") == 1
    assert remove("   title3   ") == 2
    with pytest.raises(ValueError):
        remove("title4")
        remove("")


def test_change():
    todo_list.append(ToDoList("title", 1, "type", "details"))
    todo_list.append(ToDoList("title2", 2, "type2", "details2"))
    todo_list.append(ToDoList("title3", 3, "type3", "details3"))
    titles.append("title")
    titles.append("title2")
    titles.append("title3")
    a, b, c = change("title, title, newtitle")
    assert a == "title"
    assert b == "newtitle"
    assert c == 0
    with pytest.raises(NameError):
        change("title2, title, newtitle2")
        change("title3, priority, 11")
        change("title2, invalid, newtitle2")