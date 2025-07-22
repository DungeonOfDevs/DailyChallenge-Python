# Swap First and Last Characters

# Challenge (Easy)

# Create a function named swap_characters that receives input_string as its parameter.

# This function aims to create a new string by swapping the first and last characters of the given input_string.

# To achieve this, follow these steps:

# 1. Check if the length of the input_string is less than 2. If so, return the input_string as is since swapping is not possible.
# 2. Store the first character of the input_string in a variable.
# 3. Replace the first character of the input_string with the last character.
# 4. Replace the last character of the input_string with the stored first character.
# 5. Return the modified input_string.

# Parameter:

#  -> input_string (str): The input string that needs to have its first and last characters swapped.

# The function should return a string with the first and last characters of the input_string swapped.

######################################################################################################################################

# Solution 1

def swap_characters(input_string):
    # Write code here 
    if len(input_string) < 2:
        return input_string
    
    first_character = input_string[0]
    last_character = input_string[-1]
    middle_part = input_string[1:-1]

    swapped = last_character + middle_part + first_character
    return swapped

text = input()
result = swap_characters(text)
print(result)

#######################################################################################################################################

# Solution 2

def swap_character(input_string):
    # Write code here 
    if len(input_string) < 2:
        return input_string
    else:
        first_character = input_string[0]
        last_character = input_string[-1]
        middle_part = input_string[1:-1]

        swapped = last_character + middle_part + first_character
        return swapped