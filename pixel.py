# Challenge

# Medium
# Computer screens display images by representing each pixel with three color values: red, green, and blue (RGB).
# Each color is represented by an integer value ranging from 0 to 255.

# Develop a function named string_to_rgb that takes a string and returns a list of three integers representing the red, green, and blue values of the string's RGB color.
# The function should return [0, 0, 0] if the input string is empty or contains any non-alphabetic characters.

# When mapping a string to RGB values:

#   1. Each letter is assigned a numeric value based on its position in the alphabet (a is 1, b is 2, etc.).
#   2. This numeric value is multiplied by specific factors (1 for red, 2 for green, and 3 for blue).
#   3. The resulting values are accumulated for the red, green, and blue components.
#   4. Ensure each component stays within the range of 0 to 255.
#   5 The final RGB color is returned as a list: [red, green, blue]

# The mapping is case-insensitive, so both uppercase and lowercase letters are treated the same.

##############################################################################################################################################################################

def string_to_rgb(input_string):
    # Write code here
    