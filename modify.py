import pandas as pd

# Converts from American odds to decimal odds
def converti_quote(quote_americane):
    if isinstance(quote_americane, (int, float)):
        if quote_americane > 0:
            return quote_americane / 100 + 1
        else:
            return 100 / abs(quote_americane) + 1
    else:
        return quote_americane
# Load the Excel file into a dictionary of DataFrames
input_file = "output.xlsx"
df_dict = pd.read_excel(input_file, sheet_name=None)

# Name of the outpute file
output_file = "output2.xlsx"

# Use pd.ExcelWriter to write to the sheets of an Excel file
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    # Iterate through each sheet in the dictionary
    for sheet_name, df in df_dict.items():
        # Execute the conversion function on all elements of the DataFrame, except missing and non-numeric values
        df = df.drop(index=1)
        df = df.drop(columns=df.columns[0])
        
        df.columns = df.iloc[0]
        df = df[1:]
        df.reset_index(drop=True, inplace=True)
        
        # Apply the conversion function to all elements of the DataFrame, except missing and non-numeric
        df = df.applymap(lambda x: converti_quote(x) if pd.notnull(x) else x)
        
        # Save the converted DataFrame to the Excel file with the same sheet name
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"Conversione completata per il foglio {sheet_name}")

print("Operazione completata.")