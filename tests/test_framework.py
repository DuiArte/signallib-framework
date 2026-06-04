"""test_framework.py — contract smoke tests for the public framework.

Run with: pytest -q
These assert the API contracts hold; they do not test any private survivor.
"""
from examples.example_momentum_feature import Momentum12_1
from examples.example_screen import LiquidityScreen


def test_momentum_skips_recent_month():
    # 14 monthly prices; 12-1 uses series[-13] -> series[-2]
    prices = {"ASSET_A": [100, 101, 102, 103, 104, 105, 106,
                          107, 108, 109, 110, 111, 112, 999]}
    feat = Momentum12_1()
    out = feat.compute(prices)
    # window is index -13 (=101) to -2 (=112); the 999 spike is ignored
    assert abs(out["ASSET_A"] - (112 / 101 - 1.0)) < 1e-9


def test_momentum_needs_min_history():
    feat = Momentum12_1()
    assert feat.compute({"ASSET_A": [100, 101]}) == {}


def test_liquidity_screen_floor():
    screen = LiquidityScreen(floor=1_000_000)
    mask = screen.passes({"ASSET_A": 2_000_000, "ASSET_B": 500_000})
    assert mask == {"ASSET_A": True, "ASSET_B": False}
    assert screen.apply(["ASSET_A", "ASSET_B"], {"ASSET_A": 2_000_000,
                                                 "ASSET_B": 500_000}) == ["ASSET_A"]
