import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'PinPong'


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.02)
        self.change_x = 3.5
        self.change_y = 3.5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left < 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom < 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.30)

    def update(self):
        self.center_x += self.change_x

        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left < 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom < 0:
            self.change_y = -self.change_y


class Game(arcade.Window):
    def __init__(self, widht, height, title):
        super().__init__(widht, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):  # class который центрирует все
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 3

    def on_draw(self):  # чтобы было все на экране
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y == -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.bar.change_x = 5
        if symbol == arcade.key.A:
            self.bar.change_x = -5

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D or symbol == arcade.key.A:
            self.bar.change_x = 0


if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
