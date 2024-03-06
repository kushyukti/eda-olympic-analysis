import streamlit as st
import pandas as pd
import preprocessor,helper
# import plotly as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)
st.sidebar.title('Olympics Analysis')


user_menu =st.sidebar.radio('Select an Option',('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis'))

# st.dataframe(df)


if(user_menu) == 'Medal Tally':
  st.header('Medal Tally')

  st.sidebar.header('Medal Tally')

  years, country = helper.country_year_list(df)

  selected_year = st.sidebar.selectbox('Select Year',years)
  selected_country = st.sidebar.selectbox('Select country',country)
  medal_tally =helper.fetch_medal_tally(df,selected_year ,selected_country)

  if (selected_year == 'Overall' and selected_country == 'Overall'):
    st.title('Overall Tally')
  if (selected_year != 'Overall' and selected_country == 'Overall'):
    st.title('Medal Tally in '+  str(selected_year) + ' Olympics' )
  if (selected_year == 'Overall' and selected_country != 'Overall'):
    st.title(str(selected_country) +' Overall Performance')
  if (selected_year != 'Overall' and selected_country != 'Overall'):
    st.title(str(selected_country) +  ' performance in ' + str(selected_year)+' Olympics')

  

  st.table(medal_tally)


if user_menu == 'Overall Analysis':
  st.title("Top Statistics")



  editions = df['Year'].unique().shape[0] -1
  cities = df['City'].unique().shape[0]
  sports = df['Sport'].unique().shape[0]
  events = df['Event'].unique().shape[0]
  athletes = df['Name'].unique().shape[0]
  nations = df['region'].unique().shape[0]
  
  col1, col2, col3  = st.columns(3)
  with col1:
    st.header("Editions")
    st.title(editions)
  with col2:
    st.header("Hosts")
    st.title(cities)
  with col3:
    st.header("Sports")
    st.title(sports)
    
  col1, col2, col3  = st.columns(3)
  with col1:
    st.header("Events")
    st.title(events)
  with col2:
    st.header("Athletes")
    st.title(athletes)
  with col3:
    st.header("Countries")
    st.title(nations)


  
  nations_over_time = helper.data_over_time(df,'region')
  # fig = px.line(nations_over_time, x="Editions", y="region")
  # st.title("Participating Nations over the years")
  # st.plotly_chart(fig)
  nations_over_time.rename(columns={'region':'No of Countries'},inplace=True)

  # nations_over_time

  fig , ax = plt.subplots()
  ax.plot(nations_over_time['Editions'],nations_over_time['No of Countries'])
  ax.set_xlabel('Editions')
  ax.set_ylabel('No of Countries')
  ax.set_title('Region over time')
  st.pyplot(fig)

  events_over_time = helper.data_over_time(df, 'Event')
  # events_over_time
  
  fig , ax = plt.subplots()
  ax.plot(events_over_time['Editions'],events_over_time['Event'])
  ax.set_xlabel('Editions')
  ax.set_ylabel('Event')
  ax.set_title('Events over the years')
  st.pyplot(fig)


  athlete_over_time = helper.data_over_time(df, 'Name')
  fig , ax = plt.subplots()
  ax.plot(athlete_over_time['Editions'],athlete_over_time['Name'])
  ax.set_xlabel('Editions')
  ax.set_ylabel('Athletes')
  ax.set_title('Athletes over the years')
  st.pyplot(fig)

  st.title("No. of Events over time(Every Sport)")
  fig,ax = plt.subplots(figsize=(20,20))
  x = df.drop_duplicates(['Year', 'Sport', 'Event'])
  ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),annot=True)
  st.pyplot(fig)

  
  st.title("Most successful Athletes")
  sport_list = df['Sport'].unique().tolist()
  sport_list.sort()
  sport_list.insert(0,'Overall')

  # selected_sport = st.selectbox('Select a Sport',sport_list)
  # x = helper.most_successful(df,selected_sport)
  # st.table(x)






    # fig = px.line(events_over_time, x="Edition", y="Event")
    # st.title("Events over the years")
    # st.plotly_chart(fig)
    











  
if user_menu == 'Country-wise Analysis':
    st.header('bla bla')