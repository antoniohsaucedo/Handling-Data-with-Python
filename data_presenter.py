#Open the CupcakeInvoices.csv.

data = open('../CupcakeInvoices.csv')


#Loop through all the data and print each row.

for row in data:
  print(row)

#Loop through all the data and print the type of cupcakes purchased.

  for row in data:
  values = row.split(',')
  print(values[2])

#Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

for row in data:
  values = row.split(',')
  total = int(values[3]) * float(values[4])
  print(total)

#Loop through all the data, and print out the total for all invoices combined.
for row in data:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))


#Close your open file.
data.close()

#Explore the graphing tools covered in today’s lecture. See if you can implement one of them to display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.

