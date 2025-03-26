  from ursina import *

app = Ursina()

# Spieler (Box)
player = Entity(model='cube', color=color.blue, scale=(1, 2, 1), position=(0, 1, 0))
player_speed = 5
jump_height = 5

# Schwerkraft
gravity = 0.5
velocity = 0
tofife = true

# Kameraeinstellungen
camera.position = (10, 10, 10)
camera.look_at(player)

# Plattformen erstellen
platforms = [
    Entity(model='cube', color=color.green, scale=(10, 1, 10), position=(0, 0, 0)),
    Entity(model='cube', color=color.green, scale=(10, 1, 10), position=(0, 5, 0)),
    Entity(model='cube', color=color.green, scale=(10, 1, 10), position=(0, 10, 0)),
]

# Steuerung
def update():
    global velocity

    # Bewegung des Spielers
    if held_keys['a']:
        player.x -= player_speed * time.dt
    if held_keys['d']:
        player.x += player_speed * time.dt
    if held_keys['w']:
        player.z -= player_speed * time.dt
    if held_keys['s']:
        player.z += player_speed * time.dt

    # Schwerkraft anwenden
    velocity -= gravity * time.dt
    player.y += velocity * time.dt

    # Springen
    if held_keys['space'] and player.y <= 1:
        velocity = jump_height

    # Kollisionsprüfung mit Plattformen
    for platform in platforms:
        if player.intersects(platform).hit and player.y <= platform.y + 0.5:
            velocity = 0
            player.y = platform.y + 1

app.run()
