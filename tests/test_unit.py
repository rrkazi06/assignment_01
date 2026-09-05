"""Unit tests — exercise the functions in code/bill.py directly."""

import pytest

from bill import tip_amount, grand_total, split_evenly, is_generous


def test_tip_amount():
    assert tip_amount(50, 20) == 10.0
    assert tip_amount(80, 15) == 12.0
    assert tip_amount(0, 20) == 0.0


def test_grand_total():
    assert grand_total(50, 20) == 60.0
    assert grand_total(40, 10) == 44.0


def test_split_evenly():
    assert split_evenly(60, 4) == 15.0
    assert split_evenly(100, 3) == 33.33


def test_split_evenly_rejects_zero_people():
    with pytest.raises(ValueError):
        split_evenly(60, 0)


def test_is_generous():
    assert is_generous(20) is True
    assert is_generous(25) is True
    assert is_generous(19.9) is False
