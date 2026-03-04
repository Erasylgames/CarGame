from ursina import *
import random

app = Ursina()

# Жол (фон)
road = Entity(model='cube', scale=(5,0.1,50), color=color.gray, position=(0,0,0))

# Сенің машинаң
car = Entity(model='cube', color=color.blue, scale=(1,1,2), position=(0,0.5,-10))

# Қарсы машиналар
enemies = []
for i in range(2):
    enemy = Entity(model='cube', color=color.red, scale=(1,1,2),
                   position=(random.uniform(-2,2),0.5,random.uniform(10,30)))
    enemies.append(enemy)

# Ұпай
score = 0
score_text = Text(text=f'Score: {score}', position=(-0.85,0.45), origin=(0,0), scale=2, color=color.black)

# Жылдамдық
speed = 0.2

def update():
    global score, speed
    keys = held_keys
    # Машинаны қозғалу
    if keys['a']:
        car.x -= 0.2
    if keys['d']:
        car.x += 0.2

    # Қарсы машиналарды қозғалысқа келтіру
    for enemy in enemies:
        enemy.z -= speed
        if enemy.z < -20:
            enemy.z = random.uniform(10,30)
            enemy.x = random.uniform(-2,2)
            score += 1
            score_text.text = f'Score: {score}'
            if score % 5 == 0:  # әр 5 ұпай сайын жылдамдық өседі
                speed += 0.05

        # Соқтығыс тексеру
        if car.intersects(enemy).hit:
            print("GAME OVER")
            car.color = color.red
            for e in enemies:
                e.color = color.red
            application.quit()

# Камера
EditorCamera(rotation_speed=100, pan_speed=10, zoom_speed=5)

app.run()
