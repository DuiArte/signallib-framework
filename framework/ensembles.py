"""ensembles.py — the Ensemble interface.

An Ensemble combines screens and scores into a final decision. Interface only; the
production ensemble weights are the edge and stay private (not in this repository).
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Ensemble(ABC):
    """Base class for ensembles. Subclasses implement `decide()`."""

    name: str = "unnamed_ensemble"

    def __init__(self, screens=None, scores=None):
        self.screens = list(screens or [])
        self.scores = list(scores or [])

    @abstractmethod
    def decide(self, universe, data):
        """Return the final selection / weighting as {asset -> float}.

        Reference contract: apply screens to narrow the universe, then blend scores.
        The blending weights are intentionally NOT specified here.
        """
        raise NotImplementedError
