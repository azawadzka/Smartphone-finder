import pickle
import kivy

kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

import clips_interface

database = clips_interface.DataBase()


class ClickableBox(BoxLayout):

    def box_clicked(self, touch):
        if self.y < touch.y < self.y + self.height and \
                self.x + 100 < touch.x < self.x + self.width:
            return True
        return False

    def on_touch_down(self, touch):
        super(BoxLayout, self).on_touch_down(touch)
        if self.box_clicked(touch):
            for child in self.children:
                if isinstance(child, CheckBox):
                    child.active = True


class ParametersScreen(Screen):

    def __init__(self, **kwargs):
        super(ParametersScreen, self).__init__(**kwargs)
        self.ranges = None
        with open('..\data_processing\\border_values.pickle', 'rb') as handle:
            self.ranges = pickle.load(handle)
        assert self.ranges is not None

    def read_touch(self, touch):
        print(touch)

    def process_query(self):
        self.search()

    def search(self):

        self.manager.current = "result"

        operators = {"More than": "more_than", "Less than": "less_than", "Equally": "equal"}

        if self.ids.priceCheckbox.active:
            database.put_request_quantitative("request_price", self.ids.priceSlider.value,
                                              operators[self.ids.priceOperator.text])
        if self.ids.brandCheckbox.active:
            database.put_request_multivalue("request_brand", [])
        if self.ids.osCheckbox.active:
            database.put_request_multivalue("request_operating_system", ["Android", "other"])
        if self.ids.memoryCheckbox.active:
            database.put_request_quantitative("request_memory", self.ids.memorySlider.value,
                                              operators[self.ids.memoryOperator.text])
        if self.ids.ramCheckbox.active:
            database.put_request_quantitative("request_ram", self.ids.ramSlider.value,
                                              operators[self.ids.ramOperator.text])
        if self.ids.cpuCheckbox.active:
            database.put_request_quantitative("request_cpu", self.ids.cpuSlider.value,
                                              operators[self.ids.cpuOperator.text])
        if self.ids.cameraCheckbox.active:
            database.put_request_quantitative("request_camera", self.ids.cameraSlider.value,
                                              operators[self.ids.cameraOperator.text])
        if self.ids.weightCheckbox.active:
            database.put_request_quantitative("request_weight", self.ids.weightSlider.value,
                                              operators[self.ids.weightOperator.text])
        if self.ids.batteryCheckbox.active:
            database.put_request_quantitative("request_battery", self.ids.batterySlider.value,
                                              operators[self.ids.batteryOperator.text])
        if self.ids.diagonalCheckbox.active:
            database.put_request_quantitative("request_screen_diagonal", self.ids.diagonalSlider.value,
                                              operators[self.ids.diagonalOperator.text])
        if self.ids.sdCheckbox.active:
            database.put_request_binary("request_sd", 'n')
        if self.ids.bluetoothCheckbox.active:
            database.put_request_binary("request_bluetooth", 'n')
        if self.ids.gpsCheckbox.active:
            database.put_request_binary("request_gps", 'n')
        if self.ids.wifiCheckbox.active:
            database.put_request_binary("request_wifi", 'n')
        database.run()
        # process effect
        database.reset()


class Background(BoxLayout):
    pass


class ResultLabel(Label):
    pass


class ResultCaption(Label):
    pass


class ResultStackLayout(StackLayout):
    pass


class ResultBoxLayout(BoxLayout):
    pass


class ResultBox(BoxLayout):

    def __init__(self, napis="text", **kwargs):
        super(ResultBox, self).__init__(**kwargs)
        aimg = AsyncImage(
            source='https://a.allegroimg.com/s128/117e2a/087569594d68a01c40c9dbcbbb9c/P43Pro-4GB-RAM-64GB-ROM-4G-5-8inch-Smartphone',
            size_hint_x=.15)
        box = ResultBoxLayout()
        caption = ResultCaption(text="SMARTPHONE")
        box.add_widget(caption)
        stacklayout = ResultStackLayout()
        for i in range(25):
            bg = Background()
            label = ResultLabel(text="item" + str(i))
            bg.add_widget(label)
            stacklayout.add_widget(bg)
        box.add_widget(stacklayout)
        self.add_widget(aimg)
        self.add_widget(box)


class ResultsScreen(Screen):

    def switch_to_params(self):
        self.manager.current = "params"

    def generate_result(self):
        for i in range(10):
            self.ids.space_for_result.add_widget(ResultBox(napis="Label"))


class MyScreenManager(ScreenManager):
    pass


class SmartphonesApp(App):
    def build(self):
        view = Builder.load_file("view.kv")
        return view


if __name__ == "__main__":
    app = SmartphonesApp()
    app.run()
