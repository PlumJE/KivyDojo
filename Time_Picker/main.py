from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.button import MDRectangleFlatButton
from datetime import datetime

class TimePickerApp(MDApp):
    # 메인화면 ----------------------------------------------------------------------------------------------------------------------
    def build(self):
        screen = Screen()
        self.alarm_time = "Fix your time"

        # 타임픽커를 여는 버튼을 추가
        button = MDRectangleFlatButton(text='Open Time Picker', pos_hint={'center_x':0.5, 'center_y':0.5})
        button.bind(on_release=self.show_time_picker)
        screen.add_widget(button)

        # 시간을 나타내는 라벨을 추가
        self.label = MDLabel(text='Alarm : '+str(self.alarm_time), pos_hint={'center_x':0.8, 'center_y':0.4})
        screen.add_widget(self.label)

        return screen
    # 시계 ------------------------------------------------------------------------------------------------------------------------
    def show_time_picker(self, instance):
        time_dialog = MDTimePicker()
        time_dialog.set_time(self.check_alarm_time())
        time_dialog.open()

        time_dialog.bind(on_save=self.set_time)
    # 내부동작 ----------------------------------------------------------------------------------------------------------------------
    def check_alarm_time(self):
        if self.alarm_time == "Fix your time":
            set_time = datetime.strptime("00:00:00", "%H:%M:%S")
        else:
            set_time = self.alarm_time
        return set_time
    def set_time(self, instance, time):
        self.alarm_time = time
        self.label.text = 'Alarm : '+str(self.alarm_time)
if __name__=="__main__":
    TimePickerApp().run()
