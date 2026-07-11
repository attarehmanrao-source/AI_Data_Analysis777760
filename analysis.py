def analyze_data(df):
    print("\n--- Statistical Analysis ---")
    # کل سیلز
    total_sales = df['Sales'].sum()
    # اوسط سیلز
    avg_sales = df['Sales'].mean()
    # سب سے زیادہ سیلز
    max_sales = df['Sales'].max()
    
    print(f"Total Sales: {total_sales}")
    print(f"Average Sales: {avg_sales:.2f}")
    print(f"Maximum Sales: {max_sales}")
    
    # کیٹیگری کے حساب سے ڈسٹری بیوشن
    print("\nCategory Distribution:")
    print(df['Category'].value_counts())