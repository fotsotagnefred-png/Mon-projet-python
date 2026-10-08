temperature = -3

if temperature < 0:
    print(f"{temperature} °C : gel")
elif temperature < 15:
    print(f"{temperature} °C : froid")
elif temperature < 25:
    print(f"{temperature} °C : doux")
else:
    print(f"{temperature} °C : chaud")
    for temperature in [-3, 0, 15, 31]:
    if temperature < 0:
        print(f"{temperature} °C : gel")
    elif temperature < 15:
        print(f"{temperature} °C : froid")
    elif temperature < 25:
        print(f"{temperature} °C : doux")
    else:
        print(f"{temperature} °C : chaud")