import os
import matplotlib.pyplot as plt

def generate_chart(df):
    if not os.path.exists('charts'):
        os.makedirs('charts')
    
    df.groupby('Product')['Sales'].sum().plot(kind='bar', color='skyblue', figsize=(8, 6))
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig('sales_chart.png')
    plt.show()