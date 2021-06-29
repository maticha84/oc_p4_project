#! /usr/bin/env python3
# coding: utf-8
"""
Control specific for new tournament creation
"""
import re


def control_name_place_tournament(name_place):
    name_place_valid = re.search(r"[A-Za-zéùàèêëï\- ]", name_place)
    if name_place_valid is None:
        print("the entry is not valid.")
        return 0
    else:
        return 1


def control_time_control(control_time):
    control_time_valid = re.search(r'^[123]$', control_time)
    choice_control = 0
    if control_time_valid is None:
        print("You must choose between the option 1, 2 or 3")
    else:
        if control_time == '1':
            choice_control = 'bullet'
        elif control_time == '2':
            choice_control = 'blitz'
        elif control_time == '3':
            choice_control = 'quick hit'
    return choice_control


def control_number_of_round(number_of_round):
    number_valid = re.search(r'^[\d]{1,3}$', number_of_round)
    if number_valid is None:
        return 0
    else:
        return 1