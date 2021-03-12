"""Basic Unit Tests for Lambdata Package"""

from random import randint
import pytest
import numpy as np
import pandas as pd

import lambdata as ld
# from ld.class_helper_functions import DataFrameHelper
# from ld.oop_example import SocialMediaUser

from lambdata import oop_example
from lambdata import class_helper_functions

# Testing __init__ in lambdata

def test_increment_int():
    """Making sure increment works for integers"""
    x0 = 0
    y0 = ld.increment(x0)  # 1
    assert y0 == 1

    x1 = 100
    y1 = ld.increment(x1)  # 101
    assert y1 == 101


def test_increment_float():
    """Making sure increment works for floats"""
    x0 = 10.5
    y0 = ld.increment(x0)  # 11.5
    assert y0 == 11.5


def test_increment_neg_int():
    """Making sure increment works for negative integers"""
    x0 = -1
    y0 = ld.increment(x0)  # 0
    assert y0 == 0


def test_increment_neg_float():
    """Making sure increment works for negative floats"""
    x0 = -1.5
    y0 = ld.increment(x0)  # -0.5
    assert y0 == -0.5


def test_colors():
    """Testing that COLORS contains correct items"""
    assert "Cyan" in ld.COLORS
    assert "Mauve" in ld.COLORS
    assert "Blue" in ld.COLORS
    assert "Brown" not in ld.COLORS
    assert "Yelloq" not in ld.COLORS


def test_number_colors():
    """Testing  he number of elements in COLORS"""
    assert len(ld.COLORS) == 4


# Testing oop_example

user1 = oop_example.SocialMediaUser(name="Nick", location="Arizona")
user2 = oop_example.SocialMediaUser(name="Carl", location="Costa Rica", upvotes=250)


def test_SMU_constructor():
    """Testing that SMU constructor works properly"""
    # testing name
    assert user1.name.lower() == "nick"
    assert user2.name.lower() == "carl"
    # testing location
    assert user1.location.lower() == "arizona"
    assert user2.location.lower() == "costa rica"
    # testing upvotes
    assert user1.upvotes == 0  # checks default
    assert user2.upvotes == 250


def test_unpopular():
    """Testing to make sure 0 upvotes is unpopular"""
    assert isinstance(user1.is_popular(), bool)
    assert not user1.is_popular()


def test_popular():
    """Testing to make sure 250 upvotes is popular"""
    assert user1.location.lower() == "arizona"
    assert user2.is_popular()


def test_SMU_constructor_types():
    """Testing types"""
    assert isinstance(user1.name, str)
    assert isinstance(user1.location, str)
    assert isinstance(user1.upvotes, int)


# Testing class_helper_functions

test_df = pd.DataFrame(
    {
        "column 0": [np.NaN, 4, 3, 1, 4, 2, 1, 5, 5, 2],
        "column 1": [9, 1, 2, 3, 4, np.NaN, np.NaN, 0, 22, 1],
        "column 2": [10, 2, 2, 100, 1, 2, 4, 3, 1, 2],
        "column 3": [np.NaN, np.NaN, np.NaN, 44, 4, 5, 6, 2, 43, 2],
        "column 4": [5, 6, 7, 7, 3, 2, 5, 2, 4, 4],
        "column 5": [7, 8, 4, 2, 5, 6, 7, 3, 5, 6],
        "column 6": [45, 243, 5, 1, 4, 2, 3, 5, 66, 5],
        "column 7": [1, 2, np.NaN, 3, 5, 77, 88, 99, 2, 4],
        "column 8": [np.NaN, 54, 23, 1, 33, 55, 22, 1, 3, 4],
        "column 9": [3, 22, 11, 4, 5, 4, 3, 2, 1, 4],
        "column 10": [45, 33, 23, 1, 44, 33, 234, 234, 111, 3],
    }
)

addy_series = pd.Series(
    {
        0: "890 Jennifer Brooks\nNorth Janet, WY 24785",
        1: "8394 Kim Meadow\nDarrenville, AK 27389",
        2: "379 Cain Plaza\nJosephburgh, WY 06332",
        3: "5303 Tina Hill\nAudreychester, VA 97036",
    }
)

df_helper_1 = ld.class_helper_functions.DataFrameHelper()
df_helper_2 = ld.class_helper_functions.DataFrameHelper(name="Joey")


def test_DFH_constructor():
    """Testing that DFH constructor works properly"""
    assert isinstance(df_helper_1.name, str)
    assert isinstance(df_helper_2.name, str)
    assert df_helper_1.name.lower() == "frank"  # Checks default
    assert df_helper_2.name.lower() == "joey"


def test_null_count():
    """Testing that null_count helper function works properly"""
    answer = df_helper_1.null_count(test_df)
    assert answer == 8


