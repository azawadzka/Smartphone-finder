import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

import clips_interface

database = clips_interface.DataBase()


class ParametersController(Screen):
    # checkboxes
    priceCheckbox = ObjectProperty()
    brandCheckbox = ObjectProperty()
    osCheckbox = ObjectProperty()
    memoryCheckbox = ObjectProperty()
    ramCheckbox = ObjectProperty()
    cpuCheckbox = ObjectProperty()
    cameraCheckbox = ObjectProperty()
    weightCheckbox = ObjectProperty()
    batteryCheckbox = ObjectProperty()
    diagonalCheckbox = ObjectProperty()
    sdCheckbox = ObjectProperty()
    bluetoothCheckbox = ObjectProperty()
    gpsCheckbox = ObjectProperty()
    wifiCheckbox = ObjectProperty()

    # sliders
    priceSlider = ObjectProperty()
    memorySlider = ObjectProperty()
    ramSlider = ObjectProperty()
    cpuSlider = ObjectProperty()
    cameraSlider = ObjectProperty()
    weightSlider = ObjectProperty()
    batterySlider = ObjectProperty()
    diagonalSlider = ObjectProperty()

    # operators
    priceOperator = ObjectProperty()
    memoryOperator = ObjectProperty()
    ramOperator = ObjectProperty()
    cpuOperator = ObjectProperty()
    cameraOperator = ObjectProperty()
    weightOperator = ObjectProperty()
    batteryOperator = ObjectProperty()
    diagonalOperator = ObjectProperty()

    def search(self):
        print("Search")

        operators = {"More than": "more_than", "Less than": "less_than", "Equally": "equal"}

        if (self.priceCheckbox.active):
            database.put_request_quantitative("request_price", self.priceSlider.value,
                                              operators[self.priceOperator.text])
        if (self.brandCheckbox.active):
            database.put_request_multivalue("request_brand", [])
        if (self.osCheckbox.active):
            database.put_request_multivalue("request_operating_system", ["Android", "other"])
        if (self.memoryCheckbox.active):
            database.put_request_quantitative("request_memory", self.memorySlider.value,
                                              operators[self.memoryOperator.text])
        if (self.ramCheckbox.active):
            database.put_request_quantitative("request_ram", self.ramSlider.value, operators[self.ramOperator.text])
        if (self.cpuCheckbox.active):
            database.put_request_quantitative("request_cpu", self.cpuSlider.value, operators[self.cpuOperator.text])
        if (self.cameraCheckbox.active):
            database.put_request_quantitative("request_camera", self.cameraSlider.value,
                                              operators[self.cameraOperator.text])
        if (self.weightCheckbox.active):
            database.put_request_quantitative("request_weight", self.weightSlider.value,
                                              operators[self.weightOperator.text])
        if (self.batteryCheckbox.active):
            database.put_request_quantitative("request_battery", self.batterySlider.value,
                                              operators[self.batteryOperator.text])
        if (self.diagonalCheckbox.active):
            database.put_request_quantitative("request_screen_diagonal", self.diagonalSlider.value,
                                              operators[self.diagonalOperator.text])
        if (self.sdCheckbox.active):
            database.put_request_binary("request_sd", 'n')
        if (self.bluetoothCheckbox.active):
            database.put_request_binary("request_bluetooth", 'n')
        if (self.gpsCheckbox.active):
            database.put_request_binary("request_gps", 'n')
        if (self.wifiCheckbox.active):
            database.put_request_binary("request_wifi", 'n')
        database.run()
        # process effect
        database.reset()


class SmartphonesApp(App):

    def getDatabase(self, database):
        self.database = database

    def build(self):
        self.app = ParametersController()
        return self.app
