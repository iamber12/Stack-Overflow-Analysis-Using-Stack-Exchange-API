import pandas as pd
import csv
import seaborn as sns
from matplotlib import pyplot as plt

# reading data from csv
dot_net = pd.read_csv('./dotNetTagData.csv')
r = pd.read_csv('./rTagData.csv')

# adding another column with static value in order to differentiate data related to different tags
dot_net['tag'] = 'Dot Net'
r['tag'] = 'R'

# merging data
frames = [dot_net, r]
merge_df = pd.concat(frames)
merge_df

# *****Part 1 of analysis*****

# vis1 for Is Answered metric
vis1 = sns.catplot(x="tag",kind="count",hue="Is Answered",data=merge_df,legend=True).set(title='No. of posts answered/unanswered (Dot Net vs R)',xlabel='Tag',ylabel='# Posts')


# vis 2 for View Count metric
# creating intervals(bins) in order to get count of posts having view count in between each interval
bins = [0,150,300,500, 1000,3000,9000]
merge_df['View count bucket']= pd.cut(merge_df['View count'], bins)
vis2= sns.catplot(x="tag",kind='count',hue="View count bucket",data=merge_df).set(title='Posts with different view Counts (Dot Net vs R)',xlabel='Tag',ylabel='# Posts')

# vis3 for Answer Count metric
vis3= sns.catplot(x="tag",kind='count',hue="Answer Count",data=merge_df).set(title='Posts with Answer Counts (Dot Net vs R)',xlabel='Tag',ylabel='# Posts')

# vis3 for Score metric
vis4plt, vis4 = plt.subplots()
vis4= sns.stripplot(x='tag', y='Score', data=merge_df).set(title='Post Score (Dot Net vs R)',xlabel='Tag',ylabel='Score')

# vis3 for Reputation metric
vis5_1plt, vis5_1 = plt.subplots()
vis5_1= sns.barplot(x='tag', y='Owner Reputation',data=merge_df).set(title='Owner Reputation (Dot Net vs R)',xlabel='Tag',ylabel='Owner Reputation')

vis5_2= sns.catplot(x='tag', y='Owner Reputation',data=merge_df).set(title='Owner Reputation (Dot Net vs R)',xlabel='Tag',ylabel='Owner Reputation')

# *****Part 2 of analysis*****
# Plotting relation between Answer Count and Is Answered with hue as Is Answered
vis6plt, vis6 = plt.subplots()
vis6= sns.swarmplot(x="tag",y="Answer Count",hue="Is Answered",data=merge_df).set(title='Answer Count vs Is Answered (Dot Net vs R)',xlabel='Tag')


# saving above plots as png
vis1.savefig('./plots/is_answered.png')
vis2.savefig('./plots/view_count.png')
vis3.savefig('./plots/answer_count.png')
vis4plt.savefig('./plots/score.png')
vis5_1plt.savefig('./plots/reputation_1.png')
vis5_2.savefig('./plots/reputation_2.png')
vis6plt.savefig('./plots/additional.png')


# In[ ]:




