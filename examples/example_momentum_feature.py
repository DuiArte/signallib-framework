"""example_momentum_feature.py — a textbook feature, NOT a production survivor.

12-1 momentum (trailing 12-month return skipping the most recent month) is in every
quant textbook. It exists here to make the Feature API concrete, nothing more.
"""
from __future__ import annotations
from framework.features import Feature


class Momentum12_1(Feature):
    """Classic 12-1 momentum. Public, generic, deliberately unremarkable."""

    name = "momentum_12_1"

    def compute(self, prices):
        """prices: {asset -> sequence of monthly prices}, oldest first.

        Returns {asset -> trailing 12m return skipping the last month}.
        """
        out = {}
        for asset, series in prices.items():
            if len(series) < 13:
                continue
            # skip the most recent month (index -1); window is -13..-2
            start, end = series[-13], series[-2]
            out[asset] = (end / start) - 1.0 if start else 0.0
        return out
