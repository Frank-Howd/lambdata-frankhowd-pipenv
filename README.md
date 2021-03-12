# lambdata-frankhowd-pipenv
A package of modules that include Data Science helper functions 

This is my first package, and it includes some useful and general-purpose reusuable code.  
The module Class Helper Functions (class_helper_functions) includes code written to add another layer of functionality to DataFrames data and Arrays by creating class object DataFrameHelper and includes a bonus function for dealing with a Series of addresses. 

***Includes methods for DataFrameHelper class:***
   
   ```null_count       - Check a DataFrame for null values and returns the number of missing valuse```
   
   ```train_test_split - Create a train/test split function for a data frame that returns both the
                        training and test sets.  'frac' refers to the percent of data you would
                        like to set aside for training```
                        
   ```randomize        - Develop a randomization function that randomizes all of a dataframe's cells
                        then returns that randomized dataframe.  This function also accepts a
                        random seed for reproducible randomization```


***Series function:***

     ```addy_split     - Split addresses into three columns (df['city'], df['state'], df['zip']```


***Required dependencies:***
    
   ```Python3.*
    Numpy
    Pandas
    Scikit-Learn```
    

Check it out!
