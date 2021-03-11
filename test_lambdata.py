"""Basic Unit Tests for Lambdata Package"""

from random import randint
import pytest
import lambdata as ld 


def test_increment_int():
    """Making sure increment works for integers"""
    x0 = 0
    y0 = ld.increment(x0) # 1
    assert y0 == 1

    x1 = 100
    y1 = ld.increment(x1) # 101
    assert y1 == 101


def test_increment_float():
    """Making sure increment works for floats"""
    x0 = 10.5
    y0 = ld.increment(x0) # 11.5
    assert y0 == 11.5


def test_increment_neg_int():
    """Making sure increment works for negative integers"""
    x0 = -1
    y0 = ld.increment(x0) # 0
    assert y0 == 0


def test_increment_neg_float():
    """Making sure increment works for negative floats"""
    x0 = -1.5
    y0 = ld.increment(x0) # -0.5
    assert y0 == -0.5


