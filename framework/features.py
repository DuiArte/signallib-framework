"""features.py — the Feature interface.

A Feature maps market data to a per-asset numeric signal. This module publishes the
*contract* only; production feature implementations are private (see _MANIFEST.md).
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Feature(ABC):
    """Base class for all features.

    Subclasses implement `compute()`. A feature is stateless with respect to the
    universe: given price/fundamental data it returns one number per asset.
    """

    #: human-readable name, used by scores/ensembles for provenance
    name: str = "unnamed_feature"

    @abstractmethod
    def compute(self, data):
        """Return a mapping {asset -> float} (or a pandas Series).

        `data` is whatever the caller's data layer provides (prices, fundamentals).
        Implementations must be pure: no I/O, no global state.
        """
        raise NotImplementedError

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<Feature {self.name}>"
