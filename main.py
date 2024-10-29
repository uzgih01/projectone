# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add a label
        self.label = Label(
            text='Welcome to My App!',
            size_hint=(1, 0.5)
        )
        layout.add_widget(self.label)
        
        # Add a button
        button = Button(
            text='Click Me!',
            size_hint=(1, 0.5)
        )
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)
        
        return layout
    
    def on_button_press(self, instance):
        self.label.text = 'Button was pressed!'

if __name__ == '__main__':
    MainApp().run()