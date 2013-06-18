import csv

datafile = open('teams.csv', 'r')
datareader = csv.reader(datafile)
data = []
index = 0
for row in datareader:
    if index < 100: # Go over the first 100 rows only
        data.append(row)
        index += 1

#print data # print all data

print data[1][0] # print data in row index 1 and it's column index 0
