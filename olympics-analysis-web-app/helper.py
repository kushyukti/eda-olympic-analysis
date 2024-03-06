
import numpy as np


# def medal_tally(df):
#   medal_tally = df.drop_duplicates(subset=['Team','NOC','Games','Year','Season','City','Sport','Event','Medal'])

#   medal_tally = medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()

#   medal_tally['total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

#   medal_tally['Gold'] = medal_tally['Gold'].astype('int')

#   return medal_tally


def country_year_list(df):
  years = df['Year'].unique().tolist()
  years.sort()
  years.insert(0,'Overall')


  country = np.unique(df['region'].dropna().values).tolist()
  country.sort()
  country.insert(0,'Overall')

  return years,country

def fetch_medal_tally(df, year, country):

  medal_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','Season','City','Sport','Event','Medal'])
  flag = 0
  if (year == 'Overall') and country == 'Overall':
    temp_df = medal_df
  if year == 'Overall' and country != 'Overall':
    flag = 1
    temp_df = medal_df[medal_df['region'] == country]
  if year != 'Overall' and country == 'Overall':
    temp_df = medal_df[medal_df['Year'] == int(year)] 
  if year != 'Overall' and country != 'Overall':
    temp_df = medal_df[(medal_df['Year']== int(year) )& (medal_df['region']== country) ]

  if flag == 1:
      x = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()
      x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
  else:
      x = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].    sort_values('Gold',ascending=True).reset_index()
      x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

  return x 
  

def data_over_time(df,col):
  nations_over_time = df.drop_duplicates(['Year',col])['Year'].value_counts().reset_index()
  nations_over_time.rename(columns={'Year':'Editions','count':col},inplace=True)
  return nations_over_time

# def most_successful(df, sport):
#   temp_df = df.dropna(subset=['Medal'])

#   if sport != 'Overall':
#     temp_df = temp_df[temp_df['Sport'] == sport]

#   x = temp_df['Name'].value_counts().reset_index().head(15).merge(dfleft_on='index', right_on='Name', how='left')[['index', 'Name_x','Sport', 'region']].drop_duplicates('index')
#   x.rename(columns={'index': 'Name', 'Name_x': 'Medals'}, inplace=True)
#   return x