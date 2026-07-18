altitudes = [408, 35786, 2000, 20200, 340, 550]
elt_max = None
for altitude in altitudes:
    if elt_max is None or elt_max < altitude:
        elt_max = altitude
print(f"Élément max de la liste : {elt_max}")
