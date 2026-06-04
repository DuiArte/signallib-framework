"""scores.py — the Score interface.

A Score combines one or more Features into a ranking. Interface only; the production
combination logic and weights are private.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Score(ABC):
    """Base class for scores. Subclasses implement `rank()`."""

    name: str = "unnamed_score"

    def __init__(self, features):
        #: the features this score combines; combination logic is subclass-defined
        self.features = list(features)

    @abstractmethod
    def rank(self, data):
        """Return a mapping {asset -> float} where higher = more preferred."""
        raise NotImplementedError
