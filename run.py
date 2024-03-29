#!/usr/bin/env python3

"""
Entry point to the EA program.
"""

from app.app import main
from app.state.events1 import events

main(events, print_results=True, plot_results=True, plot_file='test')
