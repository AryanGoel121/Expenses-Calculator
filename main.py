import csv
from datetime import datetime
import re

# Saving file data (messages) to a variable to work upon
filePath = r"C:\Users\aryan\OneDrive\Desktop\Software Development\Expenses-Calculator\Messages.csv"
with open(filePath, 'r') as file:
    read_file = csv.DictReader(file)
    myData = list(read_file)


# RegEx pattern to find the desired amount
amount_pattern = r'\d+\.\d+'

place_pattern = r'(?=(claim))'

for msg in myData:
    word = re.search(place_pattern, msg).group()
    print(word)





def extractAmount(msg):
    amount = re.search(amount_pattern, msg).group()
    return amount

# Expense Groups
totalExpenses = 0.0  # Final total expenses
groceryLimit = 250
travelLimit = 200
groceryAmount = 0

# # Extracting the debited amount
# for msg in myData:
#     # Date format to read
#     msg_date = datetime.strptime(msg['Date'], r"%d-%m-%Y")
#     start_date = datetime.strptime('01-02-2024', r"%d-%m-%Y")
#     end_date = datetime.strptime('20-02-2024', r"%d-%m-%Y")

#     if(start_date <= msg_date <= end_date):  # Accessing transactions in a certain period of time
#         amount = extractAmount(msg['Messages'])
#         totalExpenses += float(amount)
        
#         if('FreshCo' in msg['Messages'] or 'Walmart' in msg['Messages'] or 'Dhaba Junction' in msg['Messages']):
#             groceryAmount += float(amount)
#             if(groceryAmount > groceryLimit):
#                 print("You have crossed your ${groceryLimit}!")

# print(f'\nTotal Expenses in the month of February: ${round(totalExpenses, 2)}\n')
