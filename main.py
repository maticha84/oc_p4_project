#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB
from controllers.menu_choices_main import SwitcherMainMenu as Smm
from controllers.menu_input import choice_option


if __name__ == '__main__':

    db = TinyDB('db.json')
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')
    make_documentation_help()
    main_option = None
    Smm(players_table, tournaments_table).option_selected(main_option)
    while main_option != 0:
        main_option = choice_option()
        Smm(players_table, tournaments_table).option_selected(main_option)
