import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path, sep=',')

st.markdown("<h1 style='text-align: center;'>A short study of the Tips dataset</h1>", unsafe_allow_html=True)

''
f'**The dataset is available at {path}.**'
f'**The total size of the dataset is {tips.shape[0]} row entries.**'
''

st.subheader('1. The histogram of total bill sizes')
histo = plt.figure(figsize=(10,8))
sns.histplot(data=tips, x='total_bill')
plt.xlabel('Total bill (USD)')
st.pyplot(histo)

''
st.subheader('2. The scatterplot demonstrating the relation of total bill and tips sizes')
scatter = plt.figure(figsize=(10,8))
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.xlabel('Total bill (USD)')
plt.ylabel('Tip (USD)');
st.pyplot(scatter)

''
st.subheader('Bonus. A more detailed look into the relation of total bill and tips sizes: gender and smoker/non-smoker breakdown')
males, females = tips[tips['sex'] == 'Male'], tips[tips['sex'] == 'Female']
detailed_scatter, axes = plt.subplots(1,2,figsize=(12,5))
sns.scatterplot(data=females, x='total_bill', y='tip', hue='smoker', ax=axes[0]).set(title='Female customers')
sns.scatterplot(data=males, x='total_bill', y='tip', hue='smoker', ax=axes[1]).set(title='Male customers')
for ax in axes:
    ax.set_xlabel('Total bill (USD)')
    ax.set_ylabel('Tip (USD)')
st.pyplot(detailed_scatter)
''
st.subheader('3. The mean and median total bill sizes per day of week')
days_mean = tips.groupby('day', as_index=False)['total_bill'].agg('mean')
days_median = tips.groupby('day', as_index=False)['total_bill'].agg('median')
day_indices = {'Thur':0, 'Fri':1, 'Sat':2, 'Sun':3}
days_mean['day_index'], days_median['day_index'] = days_mean['day'].map(day_indices), days_median['day'].map(day_indices)
days_mean, days_median = days_mean.sort_values(by='day_index'), days_median.sort_values(by='day_index')
mean_median, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.barplot(data=days_mean, x='day', y='total_bill', ax=axes[0])
sns.barplot(data=days_median, x='day', y='total_bill', ax=axes[1])
axes[0].set_title('Mean total bill per day')
axes[1].set_title('Median total bill per day')
for ax in axes:
    ax.set_xlabel('Day')
    ax.set_ylabel('USD')
    for i in ax.containers:
        ax.bar_label(i, label_type='edge', fmt='%.2f')
st.pyplot(mean_median)
''
st.subheader('4. The histogram showing the distribution of total bill sizes depending on the smoker status')
bill_sizes_smokers, axes = plt.subplots(1,2,figsize=(13,5))
smokers, nonsmokers = tips[tips['time'] == 'Lunch'], tips[tips['time'] == 'Dinner']
sns.histplot(data=smokers, x='total_bill', ax=axes[0])
sns.histplot(data=nonsmokers, x='total_bill', ax=axes[1])
for ax in axes:
    ax.set_xlabel('Total bill size (USD)')
axes[0].set_title('Smokers')
axes[1].set_title('Non-smokers')
st.pyplot(bill_sizes_smokers)