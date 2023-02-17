#!/usr/bin/env python3
#
# File: module_file2.py
# About: Example module file 2.
# Development: Kelly Kinney
# Date: 2023-02-17 (Feb 17th, 2023)
"""Class to say goodbye."""


class SayGoodbye:
    """Defines the goodbye functionality."""

    def __init__(self):
        """ The entry point into the program and defines module variables."""
        self.persons_name = ""

    def say_goodbye(self, input_1="Sad Jane"):
        """The method that says goodbye."""
        self.persons_name = input_1
        print(f"Goodbye, {self.persons_name}")
        return self.persons_name
