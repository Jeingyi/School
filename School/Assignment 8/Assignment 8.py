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
meal.setName('Food')
meal.setCalories(200)
meal.setType('Main Dish')
meal.setPrepTime(45)
meal.setMainIngredient('Other Food')


print(meal.getName() + ' ' + str(meal.getCalories()) + " " + meal.getType() + " " + str(meal.getPrepTime()) + "min " + meal.getMainIngredient() + " " )
