"""example_screen.py — a textbook liquidity screen, NOT a production survivor.

Keeps assets whose average traded value clears a floor. Generic by design.
"""
from __future__ import annotations
from framework.screens import Screen


class LiquidityScreen(Screen):
    """Pass assets with average dollar volume above a floor."""

    name = "liquidity_floor"

    def __init__(self, floor: float = 1_000_000.0):
        self.floor = floor

    def passes(self, data):
        """data: {asset -> avg_dollar_volume}. Returns {asset -> bool}."""
        return {asset: adv >= self.floor for asset, adv in data.items()}
