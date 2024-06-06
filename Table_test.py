import pandas as pd

# Load the SLR table from the uploaded Excel file
slr_table_file = '/Users/kosubin/Downloads/SLR table.xlsx'
slr_table_df = pd.read_excel(slr_table_file)

# Convert the SLR table DataFrame to a list of dictionaries
slr_table = []
terminals = list(slr_table_df.columns[1:])
for index, row in slr_table_df.iterrows():
    state = {k: v for k, v in row.items() if k != 'State' and not pd.isna(v)}
    slr_table.append(state)

# Output for verification
slr_table, terminals
