import subprocess
import sys
print("TERMINAL ANIMATIONS")
print("1: RICKROLL")
print("2: RUNNER")
print("3: DONUT")
print("4: PARROT")
print("Ctrl + c to exit")
opcion = int(input("Chose an option: "))
if opcion == 1:
    subprocess.run(["curl", "ascii.live/rick"])

elif opcion == 2:
    subprocess.run(["curl", "ascii.live/forrest"])

elif opcion == 3:
    subprocess.run(["curl", "ascii.live/donut"])

elif opcion == 4:
    subprocess.run(["curl", "ascii.live/parrot"])
else:
    print("INVALID OPCION")
    sys.exit()


