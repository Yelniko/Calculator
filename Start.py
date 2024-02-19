from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from Format import *

Window.size = (400, 500)


class CalculatorApp(App):
    def build(self):
        self.box_layout = BoxLayout(orientation='vertical', padding=10)
        self.element = GridLayout(cols=5, spacing=3)
        self.lis_elements = []
        self.ty = DEC()
        self.lis_button = ['A', 'HEX', 'DEC', 'OCT', 'BIN',
                           'B', ' ( ', ' ) ', ' / ', '<-',
                           'C', '7', '8', '9', ' * ',
                           'D', '4', '5', '6', ' - ',
                           'E', '1', '2', '3', ' + ',
                           'F', 'C', '0', '.', '=', ]
        self.lis_button_2 = [self.enter, self.format, self.format, self.format, self.format,
                             self.enter, self.enter, self.enter, self.enter, self.delete,
                             self.enter, self.enter, self.enter, self.enter, self.enter,
                             self.enter, self.enter, self.enter, self.enter, self.enter,
                             self.enter, self.enter, self.enter, self.enter, self.enter,
                             self.enter, self.dalit, self.enter, self.enter, self.response, ]
        self.lab = Label(text='0', font_size=40, halign='right', valign='center', size_hint=(1, .4), text_size=(400-50, 500*.4-50))
        self.box_layout.add_widget(self.lab)
        for i in range(0, len(self.lis_button)):
            self.lis_elements.append(Button(text=self.lis_button[i], disabled=self.ty.disabled[i], on_press=self.lis_button_2[i]))

        for i in self.lis_elements:
            self.element.add_widget(i)

        self.box_layout.add_widget(self.element)
        return self.box_layout

    def format(self, instance):
        formats = {'HEX': HEX(), 'DEC': DEC(), 'OCT': OCT(), 'BIN': BIN()}
        number = self.lab.text.split(' ')
        if len(number) == 1:
            number = float(self.ty.translation_10(number[0]))
        else:
            number = float(number[number.index('-')]+self.ty.translation_10(number[-1]))
        self.ty = formats[instance.text]
        if number != 0.0:
            self.lab.text = self.ty.translation(str(number)) if number >= 0 else '- '+str(self.ty.translation(str(number*-1)))
        for i in range(0, len(self.ty.disabled)):
            self.lis_elements[i].disabled = self.ty.disabled[i]

    def enter(self, instance):
        if instance.text != ' ) ':
            if self.lab.text == '0':
                self.lab.text = ''
            self.lab.text += instance.text
        else:
            number = self.lab.text.split(' ')
            if '(' in number:
                if self.lab.text == '0':
                    self.lab.text = ''
                self.lab.text += instance.text

    def delete(self, instance):
        if self.lab.text != '0' and len(self.lab.text) != 1:
            self.lab.text = self.lab.text[:-1]
        else:
            self.lab.text = '0'

    def response(self, instance):
        lis = self.lab.text.split(' ')
        lis_1 = []
        for i in lis:
            if i != '':
                if re.fullmatch(r'(^\W+$)', i) is not None:
                    lis_1.append(i)
                else:
                    lis_1.append(self.ty.translation_10(i))
        number = float(eval(''.join(lis_1)))
        self.lab.text = self.ty.translation(str(number)) if number >= 0 else '- '+str(self.ty.translation(str(number*-1)))

    def dalit(self, instance):
        self.lab.text = '0'


if __name__ == '__main__':
    CalculatorApp().run()
