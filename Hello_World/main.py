from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


#메인 스크린 안에 있는 4*4 그리드 레이아웃
class SubGrid(GridLayout):
    def __init__(self, **kwargs):
        super(SubGrid, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Kivy parrot : '))   #1행 1열에 "Kivy parrot : "이란 라벨
        self.kivy_output = Label(text='Hello, world!')  #2행 1열에 "Hello, world!"가 디폴트인 라벨
        self.add_widget(self.kivy_output)

        self.add_widget(Label(text='You : '))           #1행 2열에 "You : "이란 라벨
        self.user_input = TextInput()                   #2행 2열에 사용자의 입력을 받는 텍스트필드
        self.add_widget(self.user_input)

#앱에 먼저 등장할 메인 스크린
class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1

        self.subGrid = SubGrid()                        #위에서 정의한 4*4 서브 그리드 레이아웃
        self.add_widget(self.subGrid)                   #1행 1열에 서브 그리드 레이아웃 추가

        self.echo_button = Button(text='Talk to Kivy!') #사용자의 입력을 Kivy앵무새가 따라하게 하는 버튼
        self.echo_button.on_press = self.echo_func      #버튼에 echo_func함수를 연결
        self.echo_button.size_hint_y = 0.5              #1행 2열의 높이는 1행 1열의 높이의 반
        self.add_widget(self.echo_button)               #1행 2열에 버튼을 추가
    #사용자의 입력을 2행 1열의 라벨에 붙여넣는 동작
    def echo_func(self, *args):
        self.subGrid.kivy_output.text = self.subGrid.user_input.text    #텍스트 필드 속 문자열을 1행1열-2행1열의 라벨에 대입

#앱 전체를 상징하는 클래스
class HelloWorldApp(App):
    def build(self):
        return MainScreen(pos_hint={'center_y':0.5}, size_hint_y=0.5)   #메인스크린은 세로로 중간에 있고, 높이도 화면의 반이다
if __name__ == "__main__":
    HelloWorldApp().run()
