from vpython import canvas, sphere, box, vector, rate, color, label
import numpy as np

# 1. On force la création de la scène
scene = canvas(title='Simulation Marche Aléatoire 3D', width=800, height=600, center=vector(5,0,0))

n_etats = 10
p, q = 0.6, 0.4

# Création de la "piste"
for i in range(1, n_etats + 1):
    box(pos=vector(i, 0, 0), length=0.8, height=0.1, width=0.8, color=color.white)
    label(pos=vector(i, -0.5, 0), text=str(i), box=False)

# La puce
puce = sphere(pos=vector(5, 0.2, 0), radius=0.3, color=color.red, make_trail=True)

pos_actuelle = 5

print("Simulation lancée... Regarde ton navigateur web.")

while True:
    rate(5) 
    r = np.random.rand()
    
    if r < p and pos_actuelle < n_etats:
        pos_actuelle += 1
    elif r < p + q and pos_actuelle > 1:
        pos_actuelle -= 1
    
    puce.pos = vector(pos_actuelle, 0.2, 0)