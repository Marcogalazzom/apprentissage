def etapes_syracuse(n):
    etapes = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        etapes += 1
    return etapes

traj_plus_longue = [None, None]
for i in range(1, 101):
    traj_act = [i, etapes_syracuse(i)]
    if traj_plus_longue[0] is None or traj_act[1] > traj_plus_longue[1]:
        traj_plus_longue = traj_act

print(f"Trajectoire la plus longue pour {traj_plus_longue[0]} en {traj_plus_longue[1]} étape(s) !")
