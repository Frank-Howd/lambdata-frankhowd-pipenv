import numpy as np
import pandas as pd

# Test Data
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
print(test_df)
test_df.head()


addy_series = pd.Series(
    {
        0: "890 Jennifer Brooks\nNorth Janet, WY 24785",
        1: "8394 Kim Meadow\nDarrenville, AK 27389",
        2: "379 Cain Plaza\nJosephburgh, WY 06332",
        3: "5303 Tina Hill\nAudreychester, VA 97036",
    }
)

print(addy_series)


# 1 Tests for null count functions
# print("null_count:", null_count(test_df), end=' ')
# print("null_count_alt:", null_count_alt(test_df))

# 2 Tests for train_test_split function
# df1, df2 = train_test_split(test_df, 0.6)
# assert isinstance(df1, pd.DataFrame)
# assert isinstance(df2, pd.DataFrame)
# print(df1, '\n\n')
# print(df2)

# 3 Tests for randomize function
# print(randomize(test_df, seed=22))

# 4 Tests for addy_split
# print(addy_split(addy_series))

pass
