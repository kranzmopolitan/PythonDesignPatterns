#!/usr/bin/env python3
"""
The factory pattern is a creational design pattern that is used to deal with the issue of
creating objects without having to specify their exact classes.

Brandon Rhodes argues that it is a poor fit for Python, and that you instead can work around
it using dependency injection, or an instance or class attribute factory. The argument there is
that the factory pattern is used in languages that cannot pass classes and functions as parameters
or be stored as attributes.

Here I will implement the original form of the factory pattern. I'll explore some alternatives
in another file.
"""
from abc import ABC, abstractmethod


class Character(ABC):
    """
    An abstract class that represents a character.

    Technically... all of these methods could just be class variables...
    """
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def source_material(self) -> str:
        pass

    @abstractmethod
    def iconic_quote(self) -> str:
        pass


class AntonChigurh(Character):
    """
    Cormac McCarthy's most odious villian.
    """
    def name(self) -> str:
        return "Anton Chigurh"

    def source_material(self) -> str:
        return "No Country for Old Men (2005) by Cormac McCarthy"

    def iconic_quote(self) -> str:
        return "What's the most you've ever lost on a coin toss?"


class Bubbles(Character):
    """
    One of the PowerPuff girls.
    """
    def name(self) -> str:
        return "Bubbles"

    def source_material(self) -> str:
        return "The PowerPuff Girls (1998 - 2002)"

    def iconic_quote(self) -> str:
        return "Education is the progressive realization of our ignorance."


class CharacterFactory(ABC):
    """
    Abstract class to return a character.
    This factory doesn't maintain any of the instances it creates.
    """
    @abstractmethod
    def create_character(self) -> Character:
        pass


class AntonChigurhFactory(CharacterFactory):
    def create_character(self) -> Character:
        return AntonChigurh()


class BubblesFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Bubbles()


def read_character()
    character_factory = {
        "bubbly": BubblesFactory(),
        "scary": AntonChigurh()
    }

    character = None

    while True:
        character_type = input("What kind of character would you like today? Please pick \"bubbly\" or \"scary\".")
        if character_type in list(character_factory.keys()):
            character = character_factory[character_type].create_character()
            print(f"Your character's name is {character.name()}.\nThey are from {character.source_material()}.\n\nAn iconic quote of theirs is \'{character.iconic_quote()}\'\n\n")
        else:
            print("Hey! You didn't type the right thing... Let's try again!\n\n")

if __name__=="__main__":
    read_character()
