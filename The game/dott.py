from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

# Ursina-App starten
app = Ursina()

# Spieler als FirstPersonController
player = FirstPersonController()

# Licht
AmbientLight(color=color.rgba(255, 255, 255, 255))

# **Boden und Wände (Grundmap für CS2-Style)**
ground = Entity(model='plane', scale=20, color=color.green, collider='mesh')
wall1 = Entity(model='cube', scale=(1, 5, 20), color=color.gray, position=(-10, 2.5, 0), collider='box')
wall2 = Entity(model='cube', scale=(1, 5, 20), color=color.gray, position=(10, 2.5, 0), collider='box')
wall3 = Entity(model='cube', scale=(20, 5, 1), color=color.gray, position=(0, 2.5, -10), collider='box')
wall4 = Entity(model='cube', scale=(20, 5, 1), color=color.gray, position=(0, 2.5, 10), collider='box')

# **Zielobjekte**
targets = []
for i in range(5):
    target = Entity(model='cube', color=color.red, scale=(1, 1, 1), position=(random.uniform(-8, 8), 2.5, random.uniform(-8, 8)), collider='box')
    targets.append(target)

# **Fadenkreuz**
crosshair = Entity(parent=camera.ui, model='quad', scale=(0.01, 0.01), color=color.red)

# Ball-Liste (Schüsse)
bullets = []

# **Schießen**
def shoot():
    bullet = Entity(model='sphere', color=color.blue, scale=0.2, position=player.position + Vec3(0, 1, 0))
    bullet.velocity = camera.forward * 15
    bullets.append(bullet)

    # Prüfen, ob die Kugel ein Ziel trifft
    for target in targets:
        if bullet.intersects(target).hit:
            target.color = color.green  # Ziel getroffen
            print("Treffer!")
            destroy(bullet)

# **Update-Funktion (Schüsse bewegen)**
def update():
    for bullet in bullets:
        bullet.position += bullet.velocity * time.dt

# **Eingaben steuern**
def input(key):
    if key == 'left mouse down':
        shoot()

# Spiel starten
app.run()
