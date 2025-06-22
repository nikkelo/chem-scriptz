import numpy as np
import pandas as pd

# Pull atomic weights from local CSV file
aw_df = pd.read_csv('atomic_weights.csv')
aw_dict = aw_df.set_index('Symbol')['Atomic_Weight'].to_dict()

# Function to calculate the molecular weight
def calculate_mw(molecule):
    weight = 0.0
    i = 0
    while i < len(molecule):
        if molecule[i].isalpha():  
            symbol = molecule[i]
            i += 1
          
            if i < len(molecule) and molecule[i].islower():
                symbol += molecule[i]
                i += 1
            
            count = 1
            if i < len(molecule) and molecule[i].isdigit():
                start = i
                while i < len(molecule) and molecule[i].isdigit():
                    i += 1
                count = int(molecule[start:i])
            
            if symbol in aw_dict:
                weight += aw_dict[symbol] * count
            else:
                print(f"Atom '{symbol}' does not exist.")
    
    return weight