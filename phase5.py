import pandas as pd import matplotlib.pyplot as plt 
 
# Load CSV data 
df = pd.read_csv('data_set_5.csv') 
 
# Prepare pie chart data pe_means = df[['PE1', 'PE2', 'PE3', 'PE4']].mean() labels = pe_means.index sizes = pe_means.values 
 
# Plot pie chart fig1, ax1 = plt.subplots() colors = ['lightcoral', 'indianred', 'firebrick', 'darkred'] ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors) ax1.axis('equal') plt.title('Average PE1 to PE4 Values - Pie Chart') plt.savefig('pie_chart.png') 
 
# Plot line chart df['TIME'] = pd.to_datetime(df['TIME']) fig2, ax2 = plt.subplots() ax2.plot(df['TIME'], df['TP1'], label='TP1') ax2.plot(df['TIME'], df['TP2'], label='TP2') plt.xlabel('Time') plt.ylabel('Values') plt.title('TP1 and TP2 Over Time') plt.legend() 
plt.savefig('line_plot.png') 
 
 	 
