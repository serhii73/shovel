"""Shovel project."""
from math import pi


class Shovel:
    """Shovel parameters and actions that can be implemented with it."""

    def __init__(self, color, weight, length, diameter):
        """Shovel parameters."""
        self.color = color
        self.weight = weight
        self.length = length
        self.diameter = diameter

    def area_handle(self):
        """Area handle shovel."""
        print('Area shovel handle is {}.'.format(
            2 * pi * (self.diameter / 2) * self.length))

    def protect_me(self):
        """Protection from the robber."""
        print('Hit the robber. {} kilo - will hurt.'.format(self.weight))

    @staticmethod
    def plant_potatoes():
        """Put the potatoes."""
        print('Plant potatoes.')

    @staticmethod
    def remove_debris():
        """Remove debris."""
        print('Remove debris.')
