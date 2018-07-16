#code for removing small sentences in all the files
import csv
l=[302,303]
for k in l:
    data = csv.reader(open(str(str(k)+"_"+"output.csv") , "r"))
    new_data=[]
    for i in data:
        line = i[0].strip().split(" ")
        if(len(line)>4):
            new_data.append(i)
    
    result_file = open(str(str(k)+"_"+"output_final.csv") , "w")
    wr = csv.writer(result_file)
    for i in new_data:
        wr.writerow(i)
