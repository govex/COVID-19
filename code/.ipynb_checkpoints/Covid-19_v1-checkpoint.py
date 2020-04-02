
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
pd.set_option('display.max_columns', 500)
plotly.offline.init_notebook_mode(connected=True)


# In[2]:


df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', verify=False)
df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')


# In[3]:


#convert table
def converttable(df):
    cols=df.columns.tolist()
    pd_list=[]
    for i in range(5,df.shape[1]):
        temp_cols=cols[:4]
        temp_cols.append(cols[i])
    # print(temp_cols)
        temp_pd=df[temp_cols].copy()
        temp_pd['dt']=cols[i]
        temp_pd.rename(columns={cols[i]:'value'},inplace=True)
        pd_list.append(temp_pd)
    df_new=pd.concat(pd_list,axis=0,ignore_index=True)
    return df_new


# In[4]:


df_confirmed_new = converttable(df_confirmed)
df_deaths_new = converttable(df_deaths)


# In[5]:


#dt format
df_confirmed_new['dt']=pd.to_datetime(df_confirmed_new['dt'])
df_deaths_new['dt']=pd.to_datetime(df_deaths_new['dt'])


# In[6]:


# Rename cols
df_confirmed_new.rename(columns = {'value': 'confirmed'}, inplace = True)
df_deaths_new.rename(columns = {'value': 'deaths'}, inplace = True)


# In[7]:


# Merge two tables
df_merged = df_confirmed_new.merge(df_deaths_new[['Province/State', 'Country/Region', 'dt', 'deaths']], 
                                   on = ['Province/State', 'Country/Region', 'dt'], 
                                   how = 'inner')
df_merged = df_merged[['Province/State', 'Country/Region', 'Lat', 'Long', 'dt', 'confirmed', 'deaths']]
#df_merged.head()


# In[8]:


# Extract and aggregate data for countries with provinces

# US
df_us = df_merged[df_merged['Country/Region'] == 'US'].copy()
df_merged.drop(index = df_us.index, inplace = True)
us_agg = df_us.groupby(by = 'dt').sum().copy()
us_agg.reset_index(inplace = True)
us_agg['Lat'] = 37.0902
us_agg['Long'] = -95.7129
us_agg['Province/State'] = np.nan
us_agg['Country/Region'] = 'US'
df_merged = pd.concat([df_merged, us_agg], sort = False, ignore_index = True)

# China
df_china = df_merged[df_merged['Country/Region'] == 'China'].copy()
df_merged.drop(index = df_china.index, inplace = True)
china_agg = df_china.groupby(by = 'dt').sum()
china_agg.reset_index(inplace = True)
china_agg['Lat'] = 35.8617
china_agg['Long'] = 104.1954
china_agg['Province/State'] = np.nan
china_agg['Country/Region'] = 'China'
df_merged = pd.concat([df_merged, china_agg], sort = False, ignore_index = True)

# Canada
df_canada = df_merged[df_merged['Country/Region'] == 'Canada'].copy()
df_merged.drop(index = df_canada.index, inplace = True)
canada_agg = df_canada.groupby(by = 'dt').sum()
canada_agg.reset_index(inplace = True)
canada_agg['Lat'] = 56.1304
canada_agg['Long'] = -106.3468
canada_agg['Province/State'] = np.nan
canada_agg['Country/Region'] = 'Canada'
df_merged = pd.concat([df_merged, canada_agg], sort = False, ignore_index = True)

# Australia
df_aus = df_merged[df_merged['Country/Region'] == 'Australia'].copy()
df_merged.drop(index = df_aus.index, inplace = True)
aus_agg = df_aus.groupby(by = 'dt').sum()
aus_agg.reset_index(inplace = True)
aus_agg['Lat'] = -25.2744
aus_agg['Long'] = 133.7751
aus_agg['Province/State'] = np.nan
aus_agg['Country/Region'] = 'Australia'
df_merged = pd.concat([df_merged, aus_agg], sort = False, ignore_index = True)

# France
df_fra = df_merged[df_merged['Country/Region'] == 'France'].copy()
df_merged.drop(index = df_fra.index, inplace = True)
fra_agg = df_fra.groupby(by = 'dt').sum()
fra_agg.reset_index(inplace = True)
fra_agg['Lat'] = 46.2276
fra_agg['Long'] = 2.2137
fra_agg['Province/State'] = np.nan
fra_agg['Country/Region'] = 'France'
df_merged = pd.concat([df_merged, fra_agg], sort = False, ignore_index = True)

# Denmark
df_den = df_merged[df_merged['Country/Region'] == 'Denmark'].copy()
df_merged.drop(index = df_den.index, inplace = True)
den_agg = df_den.groupby(by = 'dt').sum()
den_agg.reset_index(inplace = True)
den_agg['Lat'] = 56.2639
den_agg['Long'] = 9.5018
den_agg['Province/State'] = np.nan
den_agg['Country/Region'] = 'Denmark'
df_merged = pd.concat([df_merged, den_agg], sort = False, ignore_index = True)

# United Kingdom
df_uk = df_merged[df_merged['Country/Region'] == 'United Kingdom'].copy()
df_merged.drop(index = df_uk.index, inplace = True)
uk_agg = df_uk.groupby(by = 'dt').sum()
uk_agg.reset_index(inplace = True)
uk_agg['Lat'] = 56.2639
uk_agg['Long'] = 9.5018
uk_agg['Province/State'] = np.nan
uk_agg['Country/Region'] = 'United Kingdom'
df_merged = pd.concat([df_merged, uk_agg], sort = False, ignore_index = True)

# Netherlands
df_net = df_merged[df_merged['Country/Region'] == 'Netherlands'].copy()
df_merged.drop(index = df_net.index, inplace = True)
net_agg = df_net.groupby(by = 'dt').sum()
net_agg.reset_index(inplace = True)
net_agg['Lat'] = 52.1326
net_agg['Long'] = 5.2913
net_agg['Province/State'] = np.nan
net_agg['Country/Region'] = 'Netherlands'
df_merged = pd.concat([df_merged, net_agg], sort = False, ignore_index = True)

# Drop column province
df_merged.drop(columns = ['Province/State'], inplace = True)


# In[9]:


# Mortality rate
df_merged['MortalityRate'] = df_merged['deaths']/df_merged['confirmed']


# In[10]:


# Days since

# Sort dataset by date ascending
df_merged.sort_values(by = 'dt', ascending = True, inplace = True)

# List of countries
country_list = df_merged['Country/Region'].unique().tolist()

# Locate day first case for each country
first_confirmed = []
first_50confirmed = []
first_10deaths = []
    
for c in country_list:
    tmp = df_merged[df_merged['Country/Region'] == c].copy()
    if (c == 'China'):
        first_confirmed.append(pd.to_datetime('2019/12/31'))
    else:
        first_confirmed.append(tmp.loc[tmp.confirmed.ne(0).idxmax(), 'dt'])
        
    first_50confirmed.append(tmp.loc[(tmp.confirmed >= 50).idxmax(), 'dt'])
    first_10deaths.append(tmp.loc[(tmp.deaths >= 10).idxmax(), 'dt'])
        

df_first = pd.DataFrame(data = {'Country/Region': country_list, 
                                'first_confirmed': first_confirmed,
                                'first_50confirmed': first_50confirmed,
                                'first_10deaths': first_10deaths,
                               } 
                       )

# Convert to datetime
df_first['first_confirmed'] = pd.to_datetime(df_first['first_confirmed'])
df_first['first_50confirmed'] = pd.to_datetime(df_first['first_50confirmed'])
df_first['first_10deaths'] = pd.to_datetime(df_first['first_10deaths'])

#df_first.head()

# Merge firsts with main table
df_merged = df_merged.merge(df_first, on = 'Country/Region', how = 'left')

# Convert data type
df_merged['dt'] = pd.to_datetime(df_merged['dt'])

# Calculate days since
df_merged['days_since_1st_conf'] = df_merged['dt'] - df_merged['first_confirmed']
df_merged['days_since_50th_conf'] = df_merged['dt'] - df_merged['first_50confirmed']
df_merged['days_since_10th_deaths'] = df_merged['dt'] - df_merged['first_10deaths']

# Transform date units
df_merged['days_since_1st_conf'] = df_merged['days_since_1st_conf'].dt.days
df_merged['days_since_50th_conf'] = df_merged['days_since_50th_conf'].dt.days
df_merged['days_since_10th_deaths'] = df_merged['days_since_10th_deaths'].dt.days

# Drop intermediate columns
#df_merged.drop(columns = ['first_confirmed', 'first_50confirmed', 'first_10deaths'], inplace = True)

#df_merged[df_merged['Country/Region'] == 'Germany'][['dt', 'confirmed', 'deaths', 'days_since_1st_conf',
#                                                     'days_since_50th_conf', 'days_since_10th_deaths']]


# In[11]:


# New cases

# Sort values
df_merged.sort_values(by = ['Country/Region', 'dt'], ascending = True, inplace = True)

# Differences
df_merged['confirmed_newcases'] = df_merged.groupby(by = ['Country/Region']).confirmed.diff()
df_merged['deaths_newcases'] = df_merged.groupby(by = ['Country/Region']).deaths.diff()

#df_merged[df_merged['Country/Region'] == 'Germany'][['dt', 'confirmed', 'confirmed_diff']]


# In[12]:


# New cases moving average
df_merged['confirmed_newcases_movavg'] = np.nan
df_merged['deaths_newcases_movavg'] = np.nan

days_num = df_merged['dt'].unique().shape[0]

for c in country_list:
    
    tmp = df_merged[df_merged['Country/Region'] == c].copy()
    tmp = tmp.sort_values(by = 'dt').reset_index()
    
    for i in range(1, days_num-1):
        
        df_merged.loc[tmp.loc[i,'index'], 'confirmed_newcases_movavg'] = ((
            tmp.loc[i-1, 'confirmed_newcases'] +
            tmp.loc[i, 'confirmed_newcases'] +
            tmp.loc[i+1, 'confirmed_newcases'] )/3) 
        
        df_merged.loc[tmp.loc[i,'index'], 'deaths_newcases_movavg'] = ((
            tmp.loc[i-1, 'deaths_newcases'] +
            tmp.loc[i, 'deaths_newcases'] +
            tmp.loc[i+1, 'deaths_newcases'] )/3)    
        

# Check
#df_merged[df_merged['Country/Region'] == 'Germany'][['dt', 'confirmed', 'confirmed_newcases', 
#                                                     'confirmed_newcases_growth', 
#                                                     'confirmed_newcases_growth_movavg']]


# In[13]:


# Open population table
df_pop = pd.read_csv('../data_tables/world_pop_by_country.csv')
df_pop.rename(columns = {'Country Name': 'Country/Region', '2018': 'population_2018'}, inplace = True)

# Merge population table
df_merged = df_merged.merge(df_pop, on = 'Country/Region', how = 'left')

#df_merged.sort_values('dt').head()


# In[14]:


# Cases by 100.000 hab.
df_merged['confirmed_by100000pop'] = df_merged['confirmed']*100000/df_merged['population_2018']
df_merged['deaths_by100000pop'] = df_merged['deaths']*100000/df_merged['population_2018']

# Drop intermediate columns
df_merged.drop(columns = ['Country Code', 'population_2018'], inplace = True)


# In[15]:


# New cases growth (new cases today divided by new cases yesterday)

df_merged['confirmed_newcases_growth'] = np.nan
df_merged['deaths_newcases_growth'] = np.nan

for c in country_list:
    
    tmp = df_merged[df_merged['Country/Region'] == c]
    tmp = tmp.sort_values(by = 'dt').reset_index()
    
    for i in range(1, days_num):
        if (tmp.loc[i-1, 'confirmed_newcases'] != 0):
            df_merged.loc[tmp.loc[i,'index'] , 'confirmed_newcases_growth'] = (
                tmp.loc[i, 'confirmed_newcases']/tmp.loc[i-1, 'confirmed_newcases'])
        else:
            df_merged.loc[tmp.loc[i,'index'] , 'confirmed_newcases_growth'] = np.nan
        if (tmp.loc[i-1, 'deaths_newcases'] != 0):
            df_merged.loc[tmp.loc[i,'index'] , 'deaths_newcases_growth'] = (
                tmp.loc[i, 'deaths_newcases']/tmp.loc[i-1, 'deaths_newcases'])
        else:
            df_merged.loc[tmp.loc[i,'index'] , 'deaths_newcases_growth'] = np.nan
        
#df_merged[df_merged['Country/Region'] == 'Germany'][['dt', 'confirmed', 'confirmed_newcases', 
#                                                     'confirmed_newcases_growth']]


# In[16]:


# New cases growth moving average

df_merged['confirmed_newcases_growth_movavg'] = np.nan
#df_merged['deaths_newcases_growth_movavg'] = np.nan

for c in country_list:
    
    tmp = df_merged[df_merged['Country/Region'] == c].copy()
    tmp = tmp.sort_values(by = 'dt').reset_index()
    
    for i in range(2, days_num-2):
        
        df_merged.loc[tmp.loc[i,'index'], 'confirmed_newcases_growth_movavg'] = ((
            tmp.loc[i-2, 'confirmed_newcases_growth'] +
            tmp.loc[i-1, 'confirmed_newcases_growth'] +
            tmp.loc[i, 'confirmed_newcases_growth'] +
            tmp.loc[i+1, 'confirmed_newcases_growth'] +
            tmp.loc[i+2, 'confirmed_newcases_growth'] )/5) 
        
        #df_merged.loc[tmp.loc[i,'index'], 'deaths_newcases_growth_movavg'] = ((
        #    tmp.loc[i-1, 'deaths_newcases_growth'] +
        #    tmp.loc[i, 'deaths_newcases_growth'] +
        #    tmp.loc[i+1, 'deaths_newcases_growth'] )/3)    
        

# Check
#df_merged[df_merged['Country/Region'] == 'Germany'][['dt', 'confirmed', 'confirmed_newcases', 
#                                                     'confirmed_newcases_growth', 
#                                                     'confirmed_newcases_growth_movavg']]


# In[17]:


# New cases by population

# Sort values
df_merged.sort_values(by = ['Country/Region', 'dt'], ascending = True, inplace = True)

# Differences
df_merged['confirmed_newcases_by100000pop'] = df_merged.groupby(by = ['Country/Region']).confirmed_by100000pop.diff()

# Moving average
# New cases moving average
df_merged['confirmed_newcases_by100000pop_movavg'] = np.nan

for c in country_list:
    
    tmp = df_merged[df_merged['Country/Region'] == c].copy()
    tmp = tmp.sort_values(by = 'dt').reset_index()
    
    for i in range(1, days_num-1):
        
        df_merged.loc[tmp.loc[i,'index'], 'confirmed_newcases_by100000pop_movavg'] = ((
            tmp.loc[i-1, 'confirmed_newcases_by100000pop'] +
            tmp.loc[i, 'confirmed_newcases_by100000pop'] +
            tmp.loc[i+1, 'confirmed_newcases_by100000pop'] )/3) 


# In[18]:


# Select data for plotting

# Data for the top 10 countries in number of confirmed cases
last_date = df_merged['dt'].max()
top10 = df_merged[df_merged['dt'] == last_date].sort_values(by = 'deaths', ascending = False).iloc[0:10, :] 
top10_country = top10['Country/Region'].values


# In[19]:


# Plotting colors
top10_col = ['#719949', '#FF6900', '#E8927C', '#A6192E', '#51284F', 
             '#A192B2', '#418FDE', '#86C8BC', '#286140', '#F1C400']

title_col = '#002D72'
subtitle_col = 'grey'
label_col = 'dimgray'
two_color_a = '#002D72'
two_color_b = '#009B77'

# Plotting fonts & sizes
#title_font = 'PT Sans Narrow'
#subtitle_font = 'PT Sans Narrow'
#label_font = 'PT Sans'
title_font = 'Open Sans'
subtitle_font = 'Open Sans'
label_font = 'Open Sans'
title_size = 24
subtitle_size = 18
label_size = 12


# In[20]:


# Plot new cases top 10 countries
data = []

for i, c in enumerate(top10_country):
    nc = df_merged[df_merged['Country/Region'] == c].confirmed_newcases_movavg
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = nc,
                           name = c+'     ',
                           marker = dict(color = top10_col[i]),
                           line = dict(width = 3),
                           hoverinfo = 'text',
                           hovertext = [c+':<br>{:.0f}'.format(i) for i in nc],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                             bgcolor = 'white',
                                             font = dict(color = top10_col[i])),
                           showlegend = True
                          )
               )
    
    
lay = go.Layout(width = 800, 
                height = 600, 
                #bargap = 0.2,
                xaxis = dict(nticks = 10,
                             ticks = 'inside',
                             ticklen = 12,
                             tickcolor = '#eee',
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = False,
                            ),
                yaxis = dict(title='Confirmed new cases',
                             type = 'linear',
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 0.0, 
                              y = -0.18,
                              orientation = 'h',
                             ),
                margin=dict(l=50, r=20, b=150, t=100, pad=0),
                annotations=[dict(x = 0.0,
                                  y = 1.2,
                                  showarrow = False,
                                  text = 'Daily confirmed new cases (5-day moving average)',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = title_font,
                                      size = title_size,
                                      color = title_col,),
                                 ),
                             dict(x = 0.0,
                                  y = 1.1,
                                  showarrow = False,
                                  text = 'Outbreak evolution for the current 10 most affected countries',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = subtitle_font,
                                      size = subtitle_size,
                                      color = subtitle_col,),
                                 ),
                             dict(x = 0.0,
                                  y = -0.18,
                                  showarrow = False,
                                  text = 'Click any country below to hide/show from the graph:',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = 12,
                                      color = 'silver',),
                                 ),
                            ],
               )

fig = dict(data=data, layout=lay)
#plotly.offline.iplot(fig)

# Save JS
plot = plotly.offline.plot({'data':data,
                            'layout':lay},
                           include_plotlyjs = False,
                           output_type = 'div',
                           config = dict(showLink = False,
                                         modeBarButtonsToRemove = ['sendDataToCloud'],
                                         displaylogo = False,
                                         responsive = True)
                          )
path = '../visuals/new_cases/'
out_file = open(path+'timeline_newcases_date_all.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[21]:


# Plot

for i, c in enumerate(top10_country):
    data = []
    nc = df_merged[df_merged['Country/Region'] == c].confirmed_newcases_movavg
    ncp = df_merged[df_merged['Country/Region'] == c].confirmed_newcases_by100000pop_movavg
    
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = nc,
                           name = '5-day moving average',
                           marker = dict(color = '#FF9E1B'),
                           hoverinfo = 'skip',
                           hovertext = ['{:.0f}'.format(i) for i in nc],
                           hoverlabel = dict(bordercolor = 'gray',
                                             bgcolor = 'white',
                                             font = dict(color = 'gray'),
                                             )
                           )
                ),
    data.append(go.Bar(x = df_merged[df_merged['Country/Region'] == c].dt,
                       y = df_merged[df_merged['Country/Region'] == c].confirmed_newcases,
                       name = 'Actual data',
                       opacity = 0.3,
                       marker = dict(color = '#FF9E1B'),
                       hoverinfo = 'y',
                       hovertext = c,
                       hoverlabel = dict(bordercolor = 'gray',
                                         bgcolor = 'white',
                                         font = dict(color = 'gray'),
                                         ),
                       )
                )
    
    lay = go.Layout(width = 600,
                    height = 500,
                    xaxis = dict(nticks = 10,
                                 ticks = 'inside',
                                 ticklen = 12,
                                 tickcolor = '#eee',
                                 rangemode = 'nonnegative',
                                 zeroline = False,
                                 showgrid = False,
                                 ),
                    yaxis = dict(title='Confirmed new cases',
                                 type = 'linear',
                                 showgrid = True,
                                 ),
                    hovermode = 'closest',
                    font = dict(size = label_size,
                                family = label_font,
                                color = label_col,
                                ),
                    showlegend = True,
                    legend = dict(x = 0.0, 
                                  y = -0.1,
                                  orientation = 'h'
                                 ),
                    margin=dict(l=50, r=20, b=100, t=50, pad=0),
               )
          
                
    fig = dict(data=data, layout=lay)
    plot = plotly.offline.plot({'data':data,
                               'layout':lay},
                               include_plotlyjs = False,
                               output_type = 'div',
                               config = dict(showLink = False,
                                             modeBarButtonsToRemove = ['sendDataToCloud'],
                                             displaylogo = False,
                                             responsive = True)
                               )
    # Save JS
    path = '../visuals/new_cases/'
    out_file = open(path+'timeline_newcases_date_'+str(i)+'.html', 'w')
    out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
    out_file.write(plot)
    out_file.write('</body><html>')
    out_file.close()
    
#plotly.offline.iplot(fig)


# In[22]:


# Data to JSON
most_recent_day = df_merged.sort_values('dt').dt.unique()[-3]
tmp = df_merged[ (df_merged['dt'] == most_recent_day) & (df_merged['Country/Region'].isin(top10_country))].copy()

def up_or_down(x):
    if (x>=1):
        return 'up'
    else:
        return 'down'

trend = tmp.apply(lambda x: up_or_down(x['confirmed_newcases_growth_movavg']), axis=1)

most_recent_day = df_merged.sort_values('dt').dt.unique()[-1]
tmp = df_merged[ (df_merged['dt'] == most_recent_day) & (df_merged['Country/Region'].isin(top10_country))].copy()
tmp.sort_values(by = 'deaths', ascending = False, inplace = True)
tmp = tmp[['Country/Region', 'days_since_1st_conf', 'first_confirmed', 
           'confirmed', 'dt', 'confirmed_newcases']]
tmp['trend'] = trend.values
tmp['graph_number'] = np.arange(10)
tmp.set_index('Country/Region', inplace = True)
tmp.rename(columns={'Country/Region': 'country',
                    'first_confirmed': 'date_first_confirmed',
                    'dt': 'date',
                   }, inplace = True)
tmp.to_json(path+'country_info.json', orient = 'columns')
#tmp


# In[23]:


#The first case of COVID-19 in [country] was reported [number of days] days ago on [date]. 
# Since then, the country has reported [case number] cases. 
# On [date], the most recent reporting date, [country] reported [number of new cases] new cases.

