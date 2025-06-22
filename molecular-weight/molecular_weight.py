from weight_calculator import calculate_mw

# ask for molecule input, doesn't check if the input is a valid molecule.
print("Enter a molecule (e.g., C6H12O6 for glucose):")
molecule = input().strip()

# call weight calculator function
molecular_weight = calculate_mw(molecule)

print(f"{molecule} molecular weight: {molecular_weight:.2f} g/mol")