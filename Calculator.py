from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

Window.size = (400, 500)


class Calculator(Screen):
    def __int__(self, name='calculator'):
        super().__int__(name=name)
        self.box_layout = BoxLayout(orientation='vertical')
        self.lis_button = ['A', '', '', 'C', '<-',
                           'B', '(', ')', '%', '/',
                           'C', '7', '8', '9', 'X',
                           'D', '4', '5', '6', '-',
                           'E', '1', '2', '3', '+',
                           'F', '+/-', '0', ',', '=',]
        self.element = GridLayout(cols=5)
        self.element.add_widget(Label(text='0'))
        for i in self.lis_button:
            self.element.add_widget(Button(text=i))

        self.box_layout.add_widget(self.element)
        self.add_widget(self.box_layout)
