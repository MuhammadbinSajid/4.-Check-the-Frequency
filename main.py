# Define the test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}

# Print the dictionary
print("Test Dictionary:", test_dict)

# Ask the user for input
word = input("Enter a word to check its frequency: ")

# Check if the word is in the dictionary and print the frequency
if word in test_dict:
    print(f"The word '{word}' appears {test_dict[word]} times.")
else:
    print(f"The word '{word}' is not in the dictionary.")
