import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Currently reads a CSV file called "spectra.csv" in the same directory. For a different spectra, just change the file. 

# Script is used for TEMPERATURE dependent spectra.

print ("Enter a title for the spectra plot:")
spectra_title = input().strip()

print ("What kind of spectra do you want to plot?")
spectra_type = input("Enter 'IR' for Infrared, 'Raman' for Raman, or 'NMR' for Nuclear Magnetic Resonance: ")

x_label = ''
if spectra_type.lower() == 'ir':
    x_label = 'Wavenumber (cm⁻¹)'
elif spectra_type.lower() == 'raman':
    x_label = 'Raman Shift (cm⁻¹)'
elif spectra_type.lower() == 'nmr':
    x_label = 'Chemical Shift (ppm)'

# read csv file and change the first column to wavenumbers
df = pd.read_csv(r'spectra.csv')
df = df.rename(columns={'Unnamed: 0': 'x_label'})

# change the data from wide format to long format 
df_long = df.melt(
    id_vars='x_label',
    var_name='temperature',
    value_name='intensity'
    )

# show the plot
sns.lineplot(x='x_label', y='intensity', hue='temperature', data=df_long)
plt.xlabel(x_label)
plt.ylabel('Intensity')
plt.title(spectra_title)
plt.legend(title='Temperature (°C)', bbox_to_anchor=(1.05, 1))  
plt.tight_layout()
plt.show()