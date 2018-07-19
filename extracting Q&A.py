import csv
import pandas as pd

l = [300,301]
for k in l:
    df = pd.read_csv(str(k)+"_TRANSCRIPT.csv",sep='\t')
    max_length =len(df)
    i = 0
    ques_list = ["why", "how", "what", "when", "which", "where", "who"]
    count = 0
    answer_arr = []
    while(i<max_length):
        if ((df.loc[i][3]).strip().split(" "))[0] in ques_list and df.loc[i][2]== "Ellie":
            count = count + 1
            temp = 0
            string = ""
            i = i + 1
            while(df.loc[i][2]!="Ellie"):
                string = string + df.loc[i][3]
                i = i + 1
            answer_arr.append(string)    
        else:
            i = i+1
    file = open(str(k)+"_processed.csv" , "w" )
    wr = csv.writer(file)
    for i in answer_arr:
        if(i != ""):
            wr.writerow([i])
    file.close()        
