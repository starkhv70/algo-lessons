# -*- coding:utf-8 -*-

"""Users representation tests."""

import pytest
from lessons.linked_list import LinkedList, Node

L_LIST_LEN = 6


@pytest.fixture
def linked_list():
    l_list = LinkedList()
    l_list.add_in_tail(Node(3))
    l_list.add_in_tail(Node(5))
    l_list.add_in_tail(Node(7))
    l_list.add_in_tail(Node(3))
    l_list.add_in_tail(Node(9))
    l_list.add_in_tail(Node(3))
    return l_list


@pytest.fixture
def linked_list_empty():
    return LinkedList()


@pytest.fixture
def linked_list_one():
    l_list = LinkedList()
    l_list.add_in_tail(Node(1))
    return l_list


def test_find_all(linked_list):
    found_nodes = linked_list.find_all(3)
    assert len(found_nodes) == 3


def test_delete(linked_list):
    linked_list.delete(5)
    assert linked_list.find(5) is None


def test_delete_all(linked_list):
    linked_list.delete(3, all=True)
    assert linked_list.find(3) is None


def test_delete_tail(linked_list):
    tail_node_value = 11
    linked_list.delete(3, all=True)
    linked_list.add_in_tail(Node(tail_node_value))
    assert linked_list.find(tail_node_value) is not None


def test_delete_one(linked_list_one):
    linked_list_one.delete(1)
    assert linked_list_one.head is None
    assert linked_list_one.tail is None


def test_len(linked_list):
    assert linked_list.len() == L_LIST_LEN


def test_insert(linked_list):
    new_node_value = 6
    after_node = linked_list.find(7)
    linked_list.insert(after_node, Node(new_node_value))
    assert linked_list.find(6).value == new_node_value
    assert linked_list.len() == L_LIST_LEN + 1


def test_insert_one(linked_list_one):
    new_node_value = 6
    inserted_node = Node(new_node_value)
    linked_list_one.insert(None, inserted_node)
    assert linked_list_one.head == inserted_node


def test_insert_empty(linked_list_empty):
    new_node_value = 6
    inserted_node = Node(new_node_value)
    linked_list_empty.insert(None, inserted_node)
    assert linked_list_empty.head == inserted_node
    assert linked_list_empty.tail == inserted_node
