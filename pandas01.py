import pandas

# Importing 'country_data.csv' file and assigning it to variable file1
file1 = pandas.read_csv("country_data.csv")

# Importing '' file and assigning it to variable file2
file2 = pandas.read_csv("diab_data.csv")

# Importing 'housing_data.csv' file and assigning it to variable file3
file3 = pandas.read_csv("housing_data.csv")

# Importing 'insurance_data.csv' file and assigning it to variable file4. 
# Gives the following error: ParserError: Error tokenizing data. C error: Expected 1 fields in line 7, saw 2
#file4 = pandas.read_csv("insurance_data.csv")

# Importing 'iris.csv' file and assigning it to variable file5
file5 = pandas.read_csv("iris.csv")

# Print content in file1 for verify it has been uploaded correctly
print(file1)
