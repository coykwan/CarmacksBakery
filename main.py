############################################
# Coy Kwan 
# cs101
# Program 1
# Created September 3rd
# Due September 4th
############################################

# Ingredients dictionaries

# Dozen cookies is
# 2 1/2 cups butter
# 2 cups sugar
# 2 Eggs
# 8 cups of flour

dozenCookies = {
    'butter': 2.5, 
    'sugar': 2,
    'eggs': 2,
    'flour': 8,
}

# Sheet cake
# 1 cup sugar
# 1/2 cups of butter
# 2 Eggs
# 1.5 cups of flour 

sheetCake = {
    'butter': .5, 
    'sugar': 1,
    'eggs': 2,
    'flour': 1.5, 
}

# Dozen Donuts
# 0.5 cups sugar
# 3 eggs
# 5 cups of flour
# .25 cup of butter

dozenDonuts = {
    'butter': .25, 
    'sugar': .5,
    'eggs': 3,
    'flour': 5, 
}

# End restart message
print('>>> ================================ RESTART ================================') 
print('>>>') 

# Welcome message
print('Welcome to Carmack\'s Bakery')

# Asking for number of baked goods, as integers
numDozenCookies = int(input('\nHow many dozen cookies? => '))
numSheetCakes = int(input('\nHow many cakes? => '))
numDozenDonuts = int(input('\nHow many dozen donuts? => '))

# Print results
print('\n\nYou will need to order')

# Butter
initialButter = (dozenCookies['butter'] * numDozenCookies) + (sheetCake['butter'] * numSheetCakes) + (dozenDonuts['butter'] * numDozenDonuts)
butter = round(initialButter, 1) 
print('%s cups of butter' % (butter))

# Sugar
initialSugar = (dozenCookies['sugar'] * numDozenCookies) + (sheetCake['sugar'] * numSheetCakes) + (dozenDonuts['sugar'] * numDozenDonuts)
sugar = round(initialSugar, 1) 
print('%s cups of sugar' % (sugar))

# Eggs
eggs = (dozenCookies['eggs'] * numDozenCookies) + (sheetCake['eggs'] * numSheetCakes) + (dozenDonuts['eggs'] * numDozenDonuts)
print('%s eggs' % (eggs))

# Flour
initialFlour = (dozenCookies['flour'] * numDozenCookies) + (sheetCake['flour'] * numSheetCakes) + (dozenDonuts['flour'] * numDozenDonuts)
flour = round(initialFlour, 1) 
print('%s cups of flour' % (flour))

# Begin restart message
print('>>>')