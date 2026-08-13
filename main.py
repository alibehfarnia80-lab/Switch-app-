from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class SwitchApp(App):
    def build(self):
        self.state = False

        layout = BoxLayout(
            orientation='vertical',
            padding=50,
            spacing=30
        )

        self.button = Button(
            text='SWITCH',
            font_size=32,
            size_hint=(1, 0.5)
        )
        self.button.bind(on_press=self.toggle)

        self.status = Label(
            text='OFF',
            font_size=48
        )

        layout.add_widget(self.button)
        layout.add_widget(self.status)

        return layout

    def toggle(self, instance):
        self.state = not self.state

        if self.state:
            self.status.text = 'ON'
        else:
            self.status.text = 'OFF'


SwitchApp().run()
