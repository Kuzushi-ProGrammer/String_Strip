# Take the following python code thst stores a string
# str = 'X-DSPAM-Confidence: 0.8475 '
# Use 'find' and string slicing to extract the portion of the string after the colon character
# Use the 'float' function to convert the extracted string into a floating point number

'''
y = txt.rstrip() # Removes certain characters from string
x = txt.find()   # Finds where a specific character is in a string (can define where)

'''


str = "X-DSPAM-Confidence: 0.8475             * wdw"

num = str.find("0")                    # The float is the 20th character in the string
print(num)
mun = str.find("5")
print(mun)

bumb = str[num:mun + 1]       # Slicing the number out of the string
print(bumb)

# bumb = str.strip("X-DSPAMConfidence: *wd")     # Strips all the characters except for the number value
# bumb = str.translate({ord(c):None for c in "X-DSPAMConfidence: "})      # Removes unnecessary characters in string (Multiple) (Use x = txt.replace() for singular characters) (ALT METHOD)

bumb = bumb.rstrip()        # Just making sure I got everything ^^
bumb = bumb.lstrip()

bumb = float(bumb)
print(bumb + 1)

input('-Press any key to continue-')
