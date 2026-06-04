"""screens.py — the Screen interface.

A Screen reduces a universe to a shortlist via a boolean mask. Interface only.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Screen(ABC):
    """Base class for screens. Subclasses implement `passes()`."""

    name: str = "unnamed_screen"

    @abstractmethod
    def passes(self, data):
        """Return a boolean mapping {asset -> bool}; True = keep in shortlist."""
        raise NotImplementedError

    def apply(self, universe, data):
        """Convenience: return the subset of `universe` that passes."""
        mask = self.passes(data)
        return [a for a in universe if mask.get(a, False)]
