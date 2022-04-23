"""Linked list representation tests."""

import pytest
from lessons.linked_list import LinkedList, Node


@pytest.fixture
def linked_list():
    l_list = LinkedList()
    l_list.add_in_tail(Node(1))
    l_list.add_in_tail(Node(3))
    l_list.add_in_tail(Node(5))
    l_list.add_in_tail(Node(7))
    l_list.add_in_tail(Node(7))
    l_list.add_in_tail(Node(9))
    return l_list


@pytest.fixture
def linked_list_empty():
    return LinkedList()


@pytest.fixture
def linked_list_one():
    l_list = LinkedList()
    l_list.add_in_tail(Node(1))
    return l_list


def test_delete(linked_list):
    linked_list.delete(7)
    assert linked_list.find(7) is not None
    assert linked_list.len() == 5


def test_delete_all(linked_list):
    linked_list.delete(7, all=True)
    assert linked_list.find(7) is None
    assert linked_list.len() == 4


def test_delete_empty(linked_list_empty):
    linked_list_empty.delete(5)
    linked_list_empty.delete(5, all=True)
    assert linked_list_empty.head is None
    assert linked_list_empty.tail is None
    assert linked_list_empty.len() == 0


def test_delete_one(linked_list_one):
    linked_list_one.delete(1, all=True)
    assert linked_list_one.head is None
    assert linked_list_one.tail is None
    assert linked_list_one.len() == 0


def test_delete_head(linked_list):
    linked_list.delete(1)
    assert linked_list.head.value == 3


def test_delete_tail(linked_list):
    linked_list.delete(9, all=True)
    assert linked_list.tail.value == 7
