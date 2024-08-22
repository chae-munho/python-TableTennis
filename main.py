from ursina import *                #공 튀기기 게임 코드

def reset():
    ball.x = 0
    ball.z = -0.2


def update():
    global dx, dz, score_a, score_b
    paddle_b.x = paddle_b.x + held_keys["right arrow"] * time.dt
    paddle_b.x = paddle_b.x - held_keys["left arrow"] * time.dt
    paddle_a.x = paddle_a.x + held_keys["d"] * time.dt
    paddle_a.x = paddle_a.x - held_keys["a"] * time.dt
    ball.x = ball.x + time.dt * dx
    ball.z = ball.z + time.dt * dz

    if abs(ball.x) > 0.4:
        dx = -dx

    if ball.z > 0.25:
        score_b = score_b + 1
        print_on_screen(f"score_a : score_b = {score_a} : {score_b}", position = (-0.85, 0.45, ), duration = 2)
        reset()
    if ball.z < -0.65:
        score_a = score_a + 1
        print_on_screen(f"score_a : score_b = {score_a} : {score_b}", position=(-0.85, 0.45,), duration=2)
        reset()

    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == paddle_a or hit_info.entity == paddle_b:
            dz = -dz


app = Ursina()

window.color = color.orange
table = Entity(model = "cube", color = color.green, scale = (10, 0.5, 14), position = (0, 0, 0), texture = "white_cube")
camera.position = (0, 15, -26)
camera.rotation_x = 30
paddle_a = Entity(parent = table, model = "cube",color = color.black, scale = (0.2, 0.03, 0.05), position = (0, 3.7, 0.22), collider = "box")
paddle_b = duplicate(paddle_a, z = -0.62)
Text(text = "player_a", scale = 2, position = (-0.1, 0.33))
Text(text = "player_b", scale = 2, position = (-0.1, -0.4))
line = Entity(parent = table, model = "quad", scale = (0.88, 0.2, 0.1), position = (0, 3.5, -0.2))
ball = Entity(parent = table, model = "sphere", scale = 0.05, color = color.red, position = (0, 3.71, -0.2), collider = "box")
dx = 0.5
dz = 0.6

score_a = 0
score_b = 0

app.run()