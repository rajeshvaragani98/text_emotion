import csv
import pandas as pd
l = [330,335,346,347,348,350,351,352,353,355,356,362,367,377,381,418,440,483]
l2= [330,335]
for k in l:
    temp =[]
    result_file = csv.reader(open(str(str(k)+"_"+"output.csv") , "r"))
    result = open(str(str(k)+"output_final.csv") , "w")
    wr = csv.writer(result)
    for i in result_file:
        if(i):
            wr.writerow(i)
