# Justice Keopaseuth
# CIS150 Mr. Marrer
# Nov. 22, 2016
# Assignment 8

#Meal Class
class Meal:
    #Name function
    def name(self):
        self.__name = ''
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    #Calories function
    def calories(self):
        self.__calories = 0
    def setCalories(self, calories):
        self.__calories = calories
    def getCalories(self):
        return self.__calories

    #Meal type function
    def mealType(self):
        self.__mealType = ''
    def setType(self, mealType):
        self.__mealType = mealType
    def getType(self):
        return self.__mealType

    #Preperation time function
    def prepTime(self):
        self.__prepTime = 0
    def setPrepTime(self, prepTime):
        self.__prepTime = prepTime
    def getPrepTime(self):
        return self.__prepTime

    #Meal Main ingredient
    def mainIngredient(self):
        self.__mainIngredient = ''
    def setMainIngredient(self, mainIngredient):
        self.__mainIngredient = mainIngredient
    def getMainIngredient(self):
        return self.__mainIngredient

meal = Meal()
secondMeal = Meal()

meal.setName('Sandwich')
meal.setCalories(200)
meal.setType('Snack')
meal.setPrepTime(10)
meal.setMainIngredient('Bread')

secondMeal.setName('BBQ Sandwich')
secondMeal.setCalories(500)
secondMeal.setType('Lunch')
secondMeal.setPrepTime(35)
secondMeal.setMainIngredient('BBQ Pork')

#Check which one has more calories
if meal.getCalories() > secondMeal.getCalories():
    first = {'Name': secondMeal.getName(),
             'Calories': secondMeal.getCalories(),
             'Type': secondMeal.getType(),
             'PrepTime': secondMeal.getPrepTime(),
             'MainIngredient': secondMeal.getMainIngredient()}

    second = {'Name': meal.getName(),
             'Calories': meal.getCalories(),
             'Type': meal.getType(),
             'PrepTime': meal.getPrepTime(),
             'MainIngredient': meal.getMainIngredient()}
else:
    first = {'Name': meal.getName(),
             'Calories': meal.getCalories(),
             'Type': meal.getType(),
             'PrepTime': meal.getPrepTime(),
             'MainIngredient': meal.getMainIngredient()}

    second = {'Name': secondMeal.getName(),
             'Calories': secondMeal.getCalories(),
             'Type': secondMeal.getType(),
             'PrepTime': secondMeal.getPrepTime(),
             'MainIngredient': secondMeal.getMainIngredient()}


#Setting up the print cards
print('Healthy Choice:')
print('||======================================||')
print('|| Name:\t\t\t\t' + first['Name'] + '\t\t||')
print('|| Calories:\t\t\t' + str(first['Calories']) + '\t\t\t\t||')
print('|| Meal Type:\t\t\t' + first['Type'] + '\t\t\t||')
print('|| Preparation Time:\t' + str(first['PrepTime']) + 'min\t\t\t||')
print('|| Main Ingredient:\t\t' + first['MainIngredient'] + '\t\t\t||')
print('||======================================||')

print('\nNot as Healthy Choice:')
print('||======================================||')
print('|| Name:\t\t\t\t' + second['Name'] + '\t||')
print('|| Calories:\t\t\t' + str(second['Calories']) + '\t\t\t\t||')
print('|| Meal Type:\t\t\t' + second['Type'] + '\t\t\t||')
print('|| Preparation Time:\t' + str(second['PrepTime']) + 'min\t\t\t||')
print('|| Main Ingredient:\t\t' + second['MainIngredient'] + '\t\t||')
print('||======================================||')
