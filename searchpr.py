import pandas as pd
df=pd.read_csv("data",encoding = "utf-8",sep="\t",skiprows=2, index_col=0)
#print(df["Σ"])
name = input("Print name:")
score = input("Print the score:")
score=float(score)
dk=df.append({'ПІБ' : name , 'Σ' : score}, ignore_index=True)
f = open("data", encoding="utf-8", mode="r")
frow = f.readline()
frow = frow.split(" ")
len1 = len(frow)
print(frow[len1 - 1])
secrow = f.readline()
secrow = secrow.split(" ")
len2 = len(secrow)
print(secrow[len2 - 1])
newdk = dk.sort_values(by=['Σ'], ascending=False)
newdk = newdk.reset_index(drop=True)
print(newdk)
#print(dk)
def checking():
    for ind in newdk.index:
         if newdk['ПІБ'][ind]==name:
             if ind< int(secrow[len1-1]):
                print("ты на бюджете")
             else:
                 print("ты лох")
    ans=input("y/n:")
checking()
