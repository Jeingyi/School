#Opening file to be parsed
flatFile = open('OrderList', 'r')
outputFile = open('MealReport', 'w')


#Declaring and setting variables
count = 1
date = '01/01/0001'
time = '00:00:00'
calories = 0
mealName = ''
line = 0

#Declaring array for future parsing
mealList = []

#While loop to parse through the text file
while line != "":
    line = flatFile.readline()

    if(line != ""):
        date = line[0:10]
        time = line[11:19]
        calories = line[75:80]
        mealName = line[24:74]
        outputFile.write("Date: " + date.strip() + ", Time: " + time.strip() + ", Meal: " + mealName + ", Calories: " + calories.strip() + "\n")

flatFile.close()
outputFile.close()

inputFile = open('MealReport', 'r')

line = 0

while line != "":
    line = inputFile.readline().strip()

    if(line != ""):
        mealList.append(line.split(','))

print(mealList)
inputFile.close()