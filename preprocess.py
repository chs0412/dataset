
import csv
 
datalist=[[]for i in range(10)]
f = open('data.csv','r')
rdr = csv.reader(f)
for line in rdr:
    datalist[0]=line
f.close()

for i in range(1,10):
    f = open('data'+str(i)+'.csv','r')
    rdr = csv.reader(f)
    for line in rdr:
        datalist[i]=line
    f.close()

cnt=0
for i in datalist:
    print("i: ",len(i))
    cnt+=len(i)

print("total: ",cnt)