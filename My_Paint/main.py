from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


#앱 속에서 실행될 그림판 위젯
class MyPaintWidget(Widget):
    #클릭한 곳에 지름 30인 원을 생성
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
    #드래그 한 궤적따라 선을 생성
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

#앱 전체를 상징하는 클래스
class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        #버튼 위젯과 그림판 위젯을 서로 합친다
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent
    def clear_canvas(self, *args):
        self.painter.canvas.clear()
if __name__ == '__main__':
    MyPaintApp().run()
