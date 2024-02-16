import csv
from datetime import datetime
import re

# Saving file data (messages) to a variable to work upon
filePath = r"C:\Users\aryan\OneDrive\Desktop\Software Development\Expenses-Calculator\Messages.csv"
with open(filePath, 'r') as file:
    read_file = csv.DictReader(file)
    myData = list(read_file)


# RegEx pattern to find the desired amount
amount_pattern = r'\d+\.\d{2}'

place_pattern = r'(?<=at\s)\w+'


# Categorizing Expenses
def categorySelector(msg):
    return re.search(place_pattern, msg).group()

# Aount Spent
def extractAmount(msg):
    amount = re.search(amount_pattern, msg).group()
    return float(amount)

# Expense Groups
totalExpenses = 0.0  # Final total expenses

groceryLimit = 250
grocerySpent = 0

travelLimit = 300
travelSpent = 0

eatOutLimit = 180
eatOutSpent = 0

miscellLimit = 400
miscellSpent = 0

groceryStores = ['FreshCO', 'Walmart', 'Fortinos', 'Sobeys', 'Food']
traverlServices = ['Presto', 'GO', 'TTC', 'York']
restaurants = ['Dhaba', 'Haveli', 'Steak']


# Extracting the debited amount
for msg in myData:
    # Date format to read
    msg_date = datetime.strptime(msg['Date'], r"%d-%m-%Y")
    start_date = datetime.strptime('01-02-2024', r"%d-%m-%Y")
    end_date = datetime.strptime('20-02-2024', r"%d-%m-%Y")

    if(start_date <= msg_date <= end_date):  # Accessing transactions in a certain period of time
        amount = extractAmount(msg['Messages'])
        totalExpenses += amount
        
        # Dividing Expenses into categories
        if(categorySelector(msg['Messages']) in groceryStores):
            grocerySpent += amount
        elif(categorySelector(msg['Messages']) in traverlServices):
            travelSpent += amount
        elif(categorySelector(msg['Messages']) in restaurants):
            eatOutSpent += amount
        else:
            miscellSpent += amount
            

print(f'Total expensed in provided period of time: ${round(totalExpenses, 2)}\n')

if(grocerySpent > groceryLimit):
    print(f"You have crossed your Grocery Limit!: ${round(grocerySpent, 2)}\n")
if(travelSpent > travelLimit):
    print(f"You have crossed your Travel Expense Limit!: ${round(travelSpent, 2)}\n")
if(eatOutSpent > eatOutLimit):
    print(f"You have crossed your Eating Out Limit!: ${round(eatOutSpent, 2)}\n")
if(miscellSpent > miscellLimit):
    print(f"You have crossed you Miscellaneous Expense Limit!: ${round(miscellSpent, 2)}")