from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButtonSpeedDial

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        def line(self):
            print("Line")

        def bar(self):
            print("Bar")

        def pie(self):
            print("Pie")

        button = MDFloatingActionButtonSpeedDial(icon="chart-areaspline",
                                                 root_button_anim=True,
                                                 data={"Line": ["chart-line", "on_press", line],
                                                       "Bar": ["chart-bar", 'on_press', bar],
                                                       "Pie": ["chart-pie", 'on_press', pie]})

        def open(self):
            print('Open')

        def close(self):
            print('Close')

        button.bind(on_open=open)
        button.bind(on_close=close)

        return button

MainApp().run()