import pandas as pd
name=input("Enter your name")
print(name.lower())
emp=int(input("Enter your employee no."))
dat=int(input("Enter the date only"))
df=pd.read_excel("shift.xlsx",sheet_name=-1)
pos=df[(df.iloc[:,1]==name) & (df.iloc[:,2]==emp)].index.tolist()
shift=df.iloc[pos[0],dat+9]
col1=df.iloc[:,dat+9]
l=col1[col1==shift].index.to_list()

for i in l:
    print(df.iloc[i,1])


