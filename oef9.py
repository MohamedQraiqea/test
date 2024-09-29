temp_celsius = float(input("Geef een temeratuur op in ceslius:>"))
temp_fahr = (temp_celsius * 9/5) + 32
temp_Kelvin = temp_fahr + 273.15
print(f"De temperatuur in Fahrenheit is; {temp_fahr:.1f}")
print(f"De temperatuur in Kelvin is; {temp_Kelvin:.1f}")