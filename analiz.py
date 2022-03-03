import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/exported_data.csv")
print(df)
df.info()
# find the null values
null_v= df.isna().sum()
print(null_v)
# delete nul values
df = df.dropna()
# verification
null_v= df.isna().sum()
print(null_v)

print(df['rating_score'].value_counts())
# delete user id
df = df.drop(['user_id'],axis=1)
#df.info()
#plt.hist(df['critic_likes'])
#plt.show()

# plt.hist2d(df['critic_likes'],df['critic_comments'])
# plt.show()

#sns.histplot(df, x = 'critic_likes', y='critic_comments', hue='rating_score', palette='viridis', kde=True)
##plt.legend(loc='upper left', title='rating_score')
#plt.show()
print(df['user_trialist'].value_counts())
sns.countplot(data=df, x="user_trialist",hue='rating_score')
plt.show()


























