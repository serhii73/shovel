# -*- coding: utf-8 -*-
"""Shovel project.

This project shows what a shovel is, why it is needed,
what can be done with it, its characteristics are shown.
"""
from math import pi


class Shovel:
    """A shovel is a tool for digging, lifting, and moving bulk materials.

    Also, a shovel is an element of self-defense.
    """

    def __init__(self, color, weight, length, diameter):
        """Shovel parameters."""
        self.color = color
        self.weight = weight
        self.length = length
        self.diameter = diameter

    def area_handle(self):
        """Area handle shovel.

        Returns:
            prints the cylinder area.

        """
        print('Area shovel handle is {}.'.format(
            2 * pi * (self.diameter / 2) * self.length))

    def protect_me(self):
        """Protection from the robber.

        Returns:
            prints the shovel weight.

        """
        print('Hit the robber. {} kilo - will hurt.'.format(self.weight))

    @staticmethod
    def plant_potatoes():
        """Put the potatoes.

        Returns:
            prints the action - plant potatoes.

        """
        print('Plant potatoes.')

    @staticmethod
    def remove_debris():
        """Remove debris.

        Returns:
            prints the action - remove debris.

        """
        print('Remove debris.')
