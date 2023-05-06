import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime



messages = ['Hi','How are you?','I\'m fine']


df = pd.read_csv('message.csv')

df_old = df

new_data = []

for i in messages:
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    message = i

    new_data.append([now,
                     message])
    

df_new = pd.DataFrame(new_data,columns=['date_time','message'])

df_gathered = pd.concat([df_old,df_new])

df_gathered.to_csv('message.csv', index=False)

# Generate a chart

fig, ax = plt.subplots(1)

x = df_gathered['message'].value_counts()['Hi']
y = df_gathered['message'].value_counts()['How are you?']

ax.plot(x,random.randint(0,10),'bo')

plt.savefig('test.png')