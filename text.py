import re

# Sample text
text = "The price is $25.50 and $50.75 for different items."

# Define the pattern
pattern = r'\d{2}\.\d{2}'

# Use re.findall to find all matches
match = re.search(pattern, text)
# result = match.group(1)

print(match)
# Print the matches
# for match in matches:
    
