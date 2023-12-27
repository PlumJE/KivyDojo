from kivy.properties import ColorProperty
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRectangleFlatButton

#메인 스크린 안에 있는 4*4 그리드 레이아웃
class SubGrid(MDGridLayout):
    def __init__(self, **kwargs):
        super(SubGrid, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(MDLabel(text='Kivy parrot : ', halign='right')) #1행 1열에 "Kivy parrot : "이란 라벨
        self.kivy_output = MDLabel(text='Hello, world!') #2행 1열에 "Hello, world!"가 디폴트인 라벨
        self.add_widget(self.kivy_output)

        self.add_widget(MDLabel(text='You : ', halign='right')) #1행 2열에 "You : "이란 라벨
        self.user_input = MDTextField() #2행 2열에 사용자의 입력을 받는 텍스트필드
        self.add_widget(self.user_input)

#앱에 먼저 등장할 메인 스크린
class MainScreen(MDGridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1
        self.subGrid = SubGrid() #1행 1열에 4*4 그리드 레이아웃
        self.add_widget(self.subGrid)

        self.echo_button = MDRectangleFlatButton(text='Talk to Kivy!', on_press=self.echo_func) #사용자의 입력을 Kivy앵무새가 따라하게 하는 버튼
        self.add_widget(self.echo_button)       #1행 2열에 버튼을 추가
    #사용자의 입력을 2행 1열의 라벨에 붙여넣는 동작
    def echo_func(self, *args):
        self.subGrid.kivy_output.text = self.subGrid.user_input.text

#앱 전체를 상징하는 클래스
class HelloWorldApp(MDApp):
    def build(self):
        return MainScreen(pos_hint={'center_y':0.5}, size_hint_y=0.5)
if __name__ == "__main__":
    HelloWorldApp().run()
