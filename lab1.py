# Ohm’s Law Calculator

# Input voltage and resistance
voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (Ohms): "))

# Calculate current using Ohm's Law: I = V / R
if resistance != 0:
    current = voltage / resistance
    print("Current (A):", current)
else:
    print("Error: Resistance cannot be zero")