import kivy

kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

import clips_interface

database = clips_interface.DataBase()


class ParametersScreen(Screen):
    print("Display Parameters Controller")

    def process_query(self):
        self.search()

    def search(self):
        print("Search")

        # go to result screen
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


class ResultsScreen(Screen):

    def switch_to_params(self):
        self.manager.current = "params"

    def generate_result(self):
        print("Generate result")
        for i in range(100):
            self.ids.space_for_result.add_widget(Button(text="Hello", size_hint_y=None, height=100))


class MyScreenManager(ScreenManager):
    pass


class SmartphonesApp(App):
    def build(self):
        view = Builder.load_file("smartphones.kv")
        return view
