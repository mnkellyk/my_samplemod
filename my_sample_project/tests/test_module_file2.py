#!/usr/bin/env python3
#
# File: test_mode_file1.py
# About: Test for example module file 1.
# Development: Kelly Kinney
# Date: 2023-02-17 (Feb 17th, 2023)
"""Test for module_file1."""
from my_sample_project.my_sample_package.module_file2 import SayGoodbye


def test_module2():
    """Test module_file1."""
    example_name = "Eunice"
    goodbye_instance = SayGoodbye()
    assert goodbye_instance.say_goodbye(example_name) == example_name
