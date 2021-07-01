#! /usr/bin/env python3
# coding: utf-8
"""
Module for views on the top of the console
"""

import platform
import os


def clean():
    """For clean the console display"""
    p = platform.system()
    commands = {"Windows": "cls", "Linux": "clear", "Darwin": "clear"}
    try:
        os.system(commands[p])
    except ValueError:  # empty string or Java os name
        print(chr(27) + "[2J")


def pre_menu(on_top):
    """ for the title of the appliance"""

    def before_menu(*args, **kwargs):
        clean()
        print(f"\033[43;35m|{'-' * 118}|\n"
              f"| @ @@ @ {' ' * 102} @ @@ @ |\n"
              f"| @@@@@@ {' ' * 102} @@@@@@ |\n"
              f"|   @@   {' ' * 39} {'#' * 22} {' ' * 39}   @@   |\n"
              f"|  @@@@  {' ' * 39} ## Chess Tournament ## {' ' * 39}"
              f"  @@@@  |\n"
              f"| @@@@@@ {' ' * 39} {'#' * 22} {' ' * 39} @@@@@@ |\n"
              f"|@@@@@@@@{' ' * 102}@@@@@@@@|\n"
              f"|{'-' * 118}|\033[0m"
              )
        on_top(*args, **kwargs)

    return before_menu


def main_menu(on_top):
    """
    print the main menu
    """

    def before_main_choice(*args, **kwargs):
        print(f"\033[35;43m|{'Principal Menu':^118}|\n"
              f"|{'-' * 118}|\033[33;45m\n|{'-' * 118}|\n"
              f"|{' ':>45}\033[91m[1]\033[33m{' Tournament gestion':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[2]\033[33m{' Players gestion':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[3]\033[33m{' Reports':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[0]\033[33m{' Exit Chess Tournament':<30s}"
              f"{' ':>40}|\n"
              f"|{'-' * 118}|\033[0m\n"
              )
        on_top(*args, **kwargs)

    return before_main_choice


def players_menu(on_top):
    """ print the player menu on the console
    """

    def before_players_choice(*args, **kwargs):
        print(f"\033[35;43m|{'Player gestion':^118}|\n"
              f"|{'-' * 118}|\033[33;45m\n|{'-' * 118}|\n"
              f"|{' ':>45}\033[91m[1]\033[33m{' Add new player':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[2]\033[33m{' View all players':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[3]\033[33m{' Modify one player':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[4]\033[33m{' Delete all players':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[0]\033[33m{' Return principal menu':<30s}"
              f"{' ':>40}|\n"
              f"|{'-' * 118}|\033[0m\n"
              )
        on_top(*args, **kwargs)

    return before_players_choice


def players_modify_menu(on_top):
    """ print the modify menu on the console
    """

    def before_modify_choice(*args, **kwargs):
        print(f"\033[35;43m|{'Modify player':^118}|\n"
              f"|{'-' * 118}|\033[33;45m\n|{'-' * 118}|\n"
              f"|{' ':>45}\033[91m[1]\033[33m"
              f"{' Choose the ID player to modify':<30s}"
              f"{' ':>39}|\n"
              f"|{' ':>45}\033[91m[0]\033[33m{' Return Player gestion':<30s}"
              f"{' ':>40}|\n"
              f"|{'-' * 118}|\033[0m\n"
              )
        on_top(*args, **kwargs)

    return before_modify_choice


def tournament_menu(on_top):
    """ print the modify menu on the console
    """

    def before_tournament_choice(*args, **kwargs):
        print(f"\033[35;43m|{'Tournament gestion':^118}|\n"
              f"|{'-' * 118}|\033[33;45m\n|{'-' * 118}|\n"
              f"|{' ':>45}\033[91m[1]\033[33m{' Add new tournament':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[2]\033[33m{' View all tournament':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[3]\033[33m{' Modify one tournament':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[0]\033[33m{' Return principal menu':<30s}"
              f"{' ':>40}|\n"
              f"|{'-' * 118}|\033[0m\n"
              )
        on_top(*args, **kwargs)

    return before_tournament_choice


def tournament_modify_menu(on_top):
    """ print the modify menu on the console
    """

    def before_modify_choice(*args, **kwargs):
        print(f"\033[35;43m|{'Modify Tournament':^118}|\n"
              f"|{'-' * 118}|\033[33;45m\n|{'-' * 118}|\n"
              f"|{' ':>45}\033[91m[1]\033[33m"
              f"{' Choose the ID tournament to modify':<30s}"
              f"{' ':>35}|\n"
              f"|{' ':>45}\033[91m[0]\033[33m"
              f"{' Return Tournament gestion':<30s}"
              f"{' ':>40}|\n"
              f"|{'-' * 118}|\033[0m\n"
              )
        on_top(*args, **kwargs)

    return before_modify_choice


def tournament_modify_sub_menu(on_top):
    """ print the modify menu on the console
    """

    def before_modify_choice(*args, **kwargs):
        print(f"\033[35;43m|{'Modify Tournament':^118}|\n"
              f"|{'-' * 118}|\033[33;45m\n|{'-' * 118}|\n"
              f"|{' ':>45}\033[91m[1]\033[33m{' Add players':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[2]\033[33m{' Starting Round':<30s}"
              f"{' ':>40}|\n"
              f"|{' ':>45}\033[91m[3]\033[33m"
              f"{' Ending Round and add results':<38s}"
              f"{' ':>32}|\n"
              f"|{' ':>45}\033[91m[0]\033[33m"
              f"{' Return Tournament gestion':<30s}{' ':>40}|\n"
              f"|{'-' * 118}|\033[0m\n"
              )
        on_top(*args, **kwargs)

    return before_modify_choice
