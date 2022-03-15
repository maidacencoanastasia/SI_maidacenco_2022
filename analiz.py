import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from imperio import BoxCoxTransformer, YeoJohnsonTransformer
from kydavra import PValueSelector

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
# print(df['user_trialist'].value_counts())
# sns.countplot(data=df, x="user_trialist",hue='rating_score')
# plt.show()
# (df
# .groupby('user_trialist')['rating_score']\
# .value_counts(normalize=True)\
# .mul(100)\
# .rename('percent')
# .reset_index()
# .pipe((sns.catplot,'data'),x="user_trialist",y = 'percent', hue='rating_score', kind='bar'))
# plt.show()
########################################################################
# (df
# .groupby('user_subscriber')['rating_score']\
# .value_counts(normalize=True)\
# .mul(100)\
# .rename('percent')
# .reset_index()
# .pipe((sns.catplot,'data'),x="user_subscriber",y = 'percent', hue='rating_score', kind='bar'))
# plt.show()
#########################################################################
'''
(df
.groupby('user_has_payment_method')['rating_score']\
.value_counts(normalize=True)\
.mul(100)\
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'),x="user_has_payment_method",y = 'percent', hue='rating_score', kind='bar'))
plt.show()

(df
.groupby('user_subscriber')['rating_score']
.value_counts(normalize=True)
.mul(100)
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'), x='user_subscriber', y='percent', hue='rating_score', kind='bar'))
#print(df.columns)
'''
'''
(df
.groupby('user_eligible_for_trial')['rating_score']
.value_counts(normalize=True)
.mul(100)
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'), x='user_eligible_for_trial', y='percent', hue='rating_score', kind='bar'))


(df
.groupby('user_has_payment_method')['rating_score']
.value_counts(normalize=True)
.mul(100)
.rename('percent')
.reset_index()
.pipe((sns.catplot,'data'), x='user_has_payment_method', y='percent', hue='rating_score', kind='bar'))

'''

print(df.columns)
'''
sns.catplot(x="rating_score", y="movie_release_year", hue= "rating_score", data = df)
plt.show()

sns.countplot(data = df, x="movie_title_language", hue="rating_score")
plt.show()

df['movie_title_language'].unique()

sns.catplot(data = df, x="rating_score",y ="movie_popularity", hue="rating_score")
plt.show()

sns.catplot(x="rating_score", y="total_number_of_lists", hue="rating_score", data = df)
plt.show()

sns.catplot(x="rating_score", y="total_list_comments", hue="rating_score", data = df)
plt.show()

sns.catplot(x="rating_score", y="total_list_followers", hue="rating_score", data = df)
plt.show()

sns.catplot(x="rating_score", y="total_list_movie_number", hue="rating_score", data = df)
plt.show()

print(df.columns)


'''
avg_list_comments = df['avg_list_comments'] = df['total_list_comments']/df['total_number_of_lists']
avg_list_followers = df['avg_list_followers'] = df['total_list_followers']/df['total_number_of_lists']
avg_list_movis_number = df['avg_list_movis_number'] = df['total_list_movie_number']/df['total_number_of_lists']

sns.catplot(x="rating_score", y="avg_list_comments", hue="rating_score", data = df)
plt.show()
sns.catplot(x="rating_score", y="avg_list_followers", hue="rating_score", data = df)
plt.show()
sns.catplot(x="rating_score", y="avg_list_movie_number", hue="rating_score", data = df)
plt.show()


print(avg_list_comments,avg_list_followers, avg_list_movis_number)
non_informative_columns = ['user_trialist','user_subscriber','user_eligible_for_trial', 'user_has_payment_method']
df = df.drop(non_informative_columns, axis = 1)
print(df.columns)

box_cox = BoxCoxTransformer()
new_df = box_cox.apply(df, columns=['critic_likes', 'critic_comments'], target='rating_score')
print(new_df)
plt.hist(new_df['critic_comments'])
plt.show()
yeo_johnson = YeoJohnsonTransformer(l=2)
#new_df = .apply(df, columns = ['critic_likes', 'critic_comments'], target = 'raiting_score')
df = df.drop(['movie_title_language'],axis =1)















