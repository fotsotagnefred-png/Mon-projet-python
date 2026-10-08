temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

moyenne = sum(temperatures) / len(temperatures)
print(f"Moyenne : {moyenne:.2f}")
print(f"Min : {min(temperatures)} / Max : {max(temperatures)}")
jours_chauds = 0
for t in temperatures:
    if t > 15:
        jours_chauds += 1
print(f"Jours > 15 °C : {jours_chauds}")