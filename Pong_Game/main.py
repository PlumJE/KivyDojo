from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_file('main_GUI.kv')


#탁구채를 상징하는 위젯
class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        #탁구공이 탁구채에 닿으면 튕기게 한다
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

#탁구공을 상징하는 위젯
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

#앱 속에서 실행될 게임 본체를 상징하는 위젯
class PongGame(Widget):
    ball = ObjectProperty(None)     #PongBall 객체이다
    player1 = ObjectProperty(None)  #PongPaddle 객체이다
    player2 = ObjectProperty(None)  #PongPaddle 객체이다

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        #탁구공이 움직이게 한다
        self.ball.move()

        #탁구공을 탁구채에 튀게 한다 
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        #탁구공이 천장/바닥에 닿으면 튕기게 한다
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        #공이 왼쪽/오른쪽 경계를 넘어서 가면 그에 따라 득점하게 한다
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

#앱 전체를 상징하는 클래스
class PongGameApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
if __name__ == '__main__':
    PongGameApp().run()
