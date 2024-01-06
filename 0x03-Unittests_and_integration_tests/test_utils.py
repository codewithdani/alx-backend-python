#!/usr/bin/env python3
"""Module documentation here."""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests case for the `access_nested_map` function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(
            self,
            nested_map,
            path,
            expected,
            ) -> None:
        """Tests `access_nested_map`'s function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])

    def test_access_nested_map_exception(
            self,
            nested_map,
            path,
            exception,
            ) -> None:
        """Tests `access_nested_map`'s with exception."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
