<sub>**DuiArte** · quantitative research · [methodology](https://github.com/DuiArte/ltcma-methodology) · [strategies](https://github.com/DuiArte/static-drift-weight) · [framework](https://github.com/DuiArte/signallib-framework)</sub>

# SignalLib Framework

**The structure of a quant signal library — features, screens, scores, ensembles — with the API and textbook examples, but none of the production survivors.**

![status](https://img.shields.io/badge/status-active-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![updated](https://img.shields.io/badge/updated-2026--06-lightgrey)

---

This repository publishes the *architecture* of a signal library: how a **feature**,
**screen**, **score**, and **ensemble** are defined and composed. It ships the base
classes and a couple of textbook example features so the API is concrete. It does
**not** ship the production survivor features, their parameters, or the ensemble
weights — those stay private.

## Concepts

| Concept | Role |
|---|---|
| **Feature** | a function of market data → a per-asset numeric signal |
| **Screen** | a boolean filter reducing a universe to a shortlist |
| **Score** | combines features into a ranking |
| **Ensemble** | combines scores/screens into a final decision |

## Layout

```
framework/   base classes + interfaces (the API)
examples/    textbook features any quant would recognize (e.g. 12-1 momentum)
tests/       smoke tests for the framework contracts
```

## What's deliberately *not* here

Every production survivor feature and its implementation, the parameter-search
results that selected them, and the ensemble weights. This repo shows *how to build*
a signal library, not *which signals work*. See [`_MANIFEST.md`](_MANIFEST.md).

## Quick start

```python
from framework.features import Feature
from examples.example_momentum_feature import Momentum12_1

feat = Momentum12_1()
signal = feat.compute(prices)   # prices: a DataFrame of asset price series
```

## License

[MIT](LICENSE) — reuse freely. (Matches the [DuiArte/terse](https://github.com/DuiArte/terse) convention.)
