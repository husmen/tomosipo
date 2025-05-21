#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for CuPy linking."""

import pytest
import tomosipo as ts
from . import skip_if_no_cuda

try:
    import cupy as cp
    cupy_present = True
except ModuleNotFoundError:
    cupy_present = False

skip_if_no_cupy = pytest.mark.skipif(not cupy_present, reason="CuPy not installed")


@skip_if_no_cupy
@skip_if_no_cuda
def test_link_cupy_non_contiguous():
    vg = ts.volume(shape=10)
    arr_full = cp.ones((vg.shape[0] * 2, vg.shape[1], vg.shape[2]), dtype=cp.float32)
    arr = arr_full[::2]
    with pytest.warns(UserWarning):
        link = ts.link(vg, arr)
    assert link.data.flags["C_CONTIGUOUS"]

