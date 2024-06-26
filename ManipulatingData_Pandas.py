# -*- coding: utf-8 -*-
"""Assignment_11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BCmlH7i6tHyg9oNAx3uY2WCE8eTuOToe

This program reads in a .CSV file which is linked to my drive. It then has 2 functions that use the dataset.

- Find() allows the user to ask for all of the values of an entry of a particular type.
- Count() allows the user to ask how many individuals have the values of an entry of a particular type.

The program accepts 3 inputs at the start:
- (1), (2), and (3). Any other input will do nothing.
- It then will guide the user with prompts for the find() function or count() function.
"""

# Import our dataset
import pandas as pd

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
data = pd.read_csv(r'/content/gdrive/My Drive/College/Spring 2024/CS 212/villagers.csv')

# Finds all of the values of an entry of a particular type
def find(df, column_name, search_value):
    # This searches the specified column_name
    # for a item that matches the search_value entered
    return df[df[column_name] == search_value]

# Finds how many individuals have the values of an entry of a particular type
def count(df, column_name, search_value):
  count = 0
  for x in df[column_name]:
    if x == search_value:
      count = count + 1
  return count

# Checks to see if a column name exists
def column_exists(df, column_name):
  #print(column_name in df.columns)
  return column_name in df.columns

# Checks to see if a data entry in a column exists
def data_exists(df, column_name, search_value):
  for x in df[column_name]:
    if x == search_value:
      return True
  return False

# Gets input from user for the key and loops if incorrect input
def get_key(df):
  # Checking if column exists
  # Breaks out of while loop when it does exist
  while True:
      key = input("What key?")
      if column_exists(df, key) == False:
        print("Error: Key doesn't exist")
      else:
        print("Searching for", key)
        return key
        break

# Gets input from user for the value and loops if incorrect input
def get_value(df, key):
  # Checking if the value exists
  # Breaks out of while loop when it does exist
  while True:
    value = input("What value?")
    if data_exists(data, key, value) == False:
      print("Error:  There are no entries with that description")
    else:
      print("Searching for", value)
      return value
      break

# Gets input from user for the return value and loops if incorrect input
def get_return_value(df):
  # Checking if column exists
  # Breaks out of while loop when it does exist
  while True:
    return_value = input("What return value?")
    if column_exists(data, return_value) == False:
      print("Error: Return value doesn't exist")
    else:
      print("Searching for", return_value)
      return return_value
      break

4# Main loop that asks for user input
while True:
  choice = input("Do you want to: (1) find (2) count (3) exit?")

  # --------- First choice -----------
  if choice == "1":
    print("Searching for...")

    # Get's input from user and saves it
    key = get_key(data)
    value = get_value(data, key)

    # Finds the results
    result = find(data, key, value)

    # Get's input on return value from user
    return_value = get_return_value(data)

    # Prints the results
    print(result[return_value].tolist())

   # --------- Second choice -----------
  elif choice == "2":

    # Gets user input from user and saves it
    key = get_key(data)
    value = get_value(data,key)

    # prints the count using the count() function
    print(count(data,key,value))

   # --------- Third choice -----------
  elif choice == "3":
    break