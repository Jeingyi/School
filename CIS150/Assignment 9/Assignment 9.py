from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainMenuOptions(FloatLayout):
    def __init__(self, **kwargs):
        super(MainMenuOptions, self).__init__(**kwargs)

        self.titleLabel = Label(text='Health Kiosk Main Menu',
                            size_hint=(.10, .10),
                            pos=(150, 500),
                            color=(255, 255, 255, 1),
                            font_size='25sp')

        self.caloriesLabel = Label(text='Look for a meal\n\r by it''s calories',
                            size_hint=(.10, .10),
                            pos=(240, 275),
                            color=(255, 255, 255, 1),
                            font_size='15sp')

        self.prepLabel = Label(text='      Look for a meal \n\rby it''s preparation time',
                            size_hint=(.10, .10),
                            pos=(250, 100),
                            color=(255, 255, 255, 1),
                            font_size='15sp')

        self.typeLabel = Label(text=' Look for a meal \n\rby it''s meal type',
                            size_hint=(.10, .10),
                            pos=(590, 275),
                            color=(255, 255, 255, 1),
                            font_size='15sp')

        self.costLabel = Label(text='Look for a meal \n\r  by it''s cost',
                            size_hint=(.10, .10),
                            pos=(590, 100),
                            color=(255, 255, 255, 1),
                            font_size='15sp')

        self.caloriesButton = Button(text='Search Meal \n\rby Calories',
                                     size_hint=(.20, .20),
                                     pos=(50, 250))

        self.prepTimeButton = Button(text='       Search Meal \n\rby Preparation Time',
                                     size_hint=(.20, .20),
                                     pos=(50, 70))

        self.mealTypeButton = Button(text='  Search Meal \n\rby Meal Type',
                                     size_hint=(.20, .20),
                                     pos=(400, 250))

        self.mealCostButton = Button(text='Search Meal by Cost',
                                     size_hint=(.20, .20),
                                     pos=(400, 70))

        self.exitButton = Button(text='Exit',
                                 size_hint=(.10, .10),
                                 pos=(650, 500))

        self.add_widget(self.titleLabel)
        self.add_widget(self.caloriesLabel)
        self.add_widget(self.prepLabel)
        self.add_widget(self.typeLabel)
        self.add_widget(self.costLabel)
        self.add_widget(self.caloriesButton)
        self.add_widget(self.prepTimeButton)
        self.add_widget(self.mealTypeButton)
        self.add_widget(self.mealCostButton)
        self.add_widget(self.exitButton)


class InProgressMessage(FloatLayout):
    def __init__(self, **kwargs):
        super(InProgressMessage, self).__init__(**kwargs)
        self.cols = 1
        self.backButton = Button(text='Back', size_hint=(.20, .20), pos=(400, 70))
        self.add_widget(self.backButton)


class MenuKiosk(App):
    def build(self):
        return MainMenuOptions()


if __name__ == '__main__':
    MenuKiosk().run()
