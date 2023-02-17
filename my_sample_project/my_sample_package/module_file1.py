#!/usr/bin/env python3
#
# File: module_file1.py
# About: Example module file 1.
# Development: Kelly Kinney
# Date: 2023-02-17 (Feb 17th, 2023)
"""Class to say hello."""


class SayHello:
    """Defines the hello functionality."""

    def __init__(self):
        """ The entry point into the program and defines module variables."""
        self.persons_name = ""

    def say_hello(self, input_1):
        """The method that says hello."""
        self.persons_name = input_1
        print(f"Hello, {self.persons_name}")
        return self.persons_name
