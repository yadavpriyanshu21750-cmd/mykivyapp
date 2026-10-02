from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.label = Label(text="Welcome to My App!", font_size='24sp')
        btn = Button(text="Click Me", size_hint=(1, 0.3), font_size='20sp')
        btn.bind(on_press=self.on_click)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_click(self, instance):
        self.label.text = "Button Clicked Successfully!"

if __name__ == '__main__':
    MyApp().run()
  
