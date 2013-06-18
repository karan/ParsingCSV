import csv

datafile = open('teams.csv', 'r')
datareader = csv.reader(datafile)
data = []
for index, row in enumerate(datareader):
    if index < 100:
        data.append(row)
datafile.close()

print str(len(data)) + " rows scraped"
#print data

writeto = open('first100.csv', 'wb') # open in binary mode
                                     # 'w' => /r/n/n --- 'wb' => /r/n
datawriter = csv.writer(writeto)
for row in data:
    datawriter.writerow(row)
    #print row
    
writeto.close()

print "file writing completed"
