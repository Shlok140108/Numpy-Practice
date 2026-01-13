# Day 4 – NumPy Memory Model & Strides

Today’s focus was understanding how NumPy handles memory internally.

## Topics Covered
- Views vs copies
- `reshape()` vs `ravel()` vs `flatten()`
- Strides and memory sharing
- When reshaping shares memory and when it creates copies

## Key Learnings
- NumPy arrays are defined by **data pointer, shape, and strides**
- Memory sharing depends on **stride compatibility**, not just contiguity
- Basic slicing usually returns views, while fancy indexing returns copies
- `ravel()` may return a view, but `flatten()` always returns a copy
- `reshape()` returns a view only if the new shape can be represented using strides

## Files
- `views_vs_copies.py` – Experiments with slicing, fancy indexing, and shared memory
- `reshape_vs_ravel_vs_flatten.py` – Behavioral differences and memory checks
- `strides_experiments.py` – Stride inspection and reshape edge cases

## Takeaway
Understanding strides is essential for writing memory-efficient NumPy code and
for contributing safely to NumPy internals.
