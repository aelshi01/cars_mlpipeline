import pandas as pd

def des_stat(file: str,col_name: str):
    filename = file
    data = pd.read_csv(filename)
    data = data[[col_name,'Iris-setosa']]

    descr_stat = pd.DataFrame.describe(data)



    return descr_stat


file = '/Users/adamelshimi/Desktop/Udacity/iris.data'

summary1 = des_stat(file,'5.1')
summary2 = des_stat(file,'3.5')
summary3 = des_stat(file,'1.4')
summary4 = des_stat(file,'0.2')
print(summary1)
print(summary2)
print(summary3)
print(summary4)