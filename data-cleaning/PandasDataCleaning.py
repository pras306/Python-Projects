import pandas as pd

df = pd.read_excel(r"C:/Users/pras3/source/Workspace/data-analyst-projects/Python-Projects/data-cleaning/Customer Call List.xlsx")

# STEP 1: DROP DUPLICATES IN DATA

df = df.drop_duplicates()

# STEP 2: DROP UNWANTED COLUMNS

df = df.drop(columns = "Not_Useful_Column")

# STEP 3: REMOVE UNWANTED TEXTS FROM LAST NAME COLUMN

# df['Last_Name'] = df['Last_Name'].str.lstrip('/')
# df['Last_Name'] = df['Last_Name'].str.lstrip('...')
# df['Last_Name'] = df['Last_Name'].str.rstrip('_')

# OR

df['Last_Name'] = df['Last_Name'].str.strip('123._/')

# STEP 4: GENERALIZE THE PHONE NUMBER FORMAT IN PHONE NUMBER COLUMN

df['Phone_Number'] = df['Phone_Number'].str.replace('[^0-9]', '')

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

df['Phone_Number'] = df['Phone_Number'].str.replace('nan', '')

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: '(' + x[0:3] + ')' + x[3:6] + '-' + x[6:] if len(x) > 0 else x)

# STEP 5: SPLIT ADDRESS COLUMN INTO 3 COLUMNS OF ADDRESSES

df[['Street_Address', 'State', 'Zip_Code' ]] =  df['Address'].str.split(',',2, expand = True)

# STEP 6: CHANGE Paying Customer and Do not Contact columns to have the same format

df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')

# STEP 7: Remove N/a and NaN values in the data set

df = df.replace('N/a', '')
df = df.fillna('')

# STEP 8: Remove Customers who DO NOT have phone numbers or have asked not to be contacted

for x in df.index:
    if df.loc[x, 'Do_Not_Contact'] == 'Y':
        df.drop(x, inplace = True)
        pass
    pass

for x in df.index:
    if df.loc[x, 'Phone_Number'] == '':
        df.drop(x, inplace = True)
        pass
    pass

# STEP 9: REMOVE the address columns

df = df.drop('Address', axis = 1)

# STEP 10: RESET the Index of the dataset

df = df.reset_index(drop = True)

# STEP 11: Write final data into a new file for further analysis

df.to_csv(r"C:/Users/pras3/source/Workspace/data-analyst-projects/Python-Projects/data-cleaning/FinalList.csv", index = False)