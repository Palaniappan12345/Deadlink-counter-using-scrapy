import pandas as pd
df = pd.read_csv("count.csv")
count = df.groupby(['Link']).count() 
#print(count)
data = pd.DataFrame(count)
data =data.drop(columns=['status'])
data.rename(columns = {'url':'Dead Link Count'}, inplace = True) 
data.to_csv('Submission.csv')
 
