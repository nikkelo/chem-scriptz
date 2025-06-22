import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ask for which compound, the given CSV is anthocyanin
print("What compound is being measured for calibration?")
compound = input().strip()

# read absorbance CSV file
df = pd.read_csv('calibration_data.csv')

# construct basic plot
sns.regplot(x="concentration", y="absorbance", data=df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Absorbance vs Concentration of " + compound) 
plt.xlabel("Concentration (μg/cm³)")
plt.ylabel("Absorbance")
plt.legend(title='Calibration Curve', loc='upper left')
plt.grid(True)

# annotated sample points
for i, row in df.iterrows():
    plt.annotate(str(row['sample']),
                 (row['concentration'], row['absorbance']),
                 textcoords="offset points", xytext=(0,10), ha='center',
                 fontsize=10)


plt.show()

