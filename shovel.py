# -*- coding: utf-8 -*-
"""Shovel module.

This module shows what a shovel is, why it is needed,
what can be done with it, its characteristics are shown.
"""
from math import pi


class Shovel:
    """A shovel is a tool for remove debris and for planting potatoes.

    Also, a shovel is an element of self-defense.
    Also, we can calculate the area of handle shovel.
    """

    def __init__(self, color, weight, length, diameter):
        """Shovel parameters."""
        self.color = color
        self.weight = weight
        self.length = length
        self.diameter = diameter

    def area_handle(self):
        """Print the cylinder(handle shovel) area."""
        print('Area shovel handle is {}.'.format(
            2 * pi * (self.diameter / 2) * self.length))

    def protect_me(self):
        """Protection from the robber.

        If the shovel is heavy, the robber can be killed.
        """
        print('Hit the robber. {} kilo - will hurt.'.format(self.weight))
        if self.weight > 5:
            print('Call 911, the robber unconscious.')

    @staticmethod
    def plant_potatoes():
        """Put the potatoes in the fertile land."""
        print('Plant potatoes on our field.')

    @staticmethod
    def remove_debris(weight_debris):
        """Remove debris.

        If debris is heavy, the shovel can break.
        """
        print('Pick up trash near our yard.')
        if weight_debris > 4:
            print('Be careful, the debris is heavy.')
