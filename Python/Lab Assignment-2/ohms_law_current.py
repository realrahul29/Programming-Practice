# ohms_law_current.py

v = float(input("Enter Voltage (V): "))
r = float(input("Enter Resistance (R): "))

current = v / r
print("Current =", current, "A")

if current < 0.5:
    print("Low current")
elif current <= 2:
    print("Normal current")
else:
    print("High current")
