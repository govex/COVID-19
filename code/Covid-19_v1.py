
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime
#import reverse_geocode
import plotly
import plotly.graph_objs as go

pd.set_option('display.max_columns', 500)
#plotly.offline.init_notebook_mode(connected=True)


# In[2]:


# Load data
df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')


# In[3]:


# Convert table
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

df_confirmed_new = converttable(df_confirmed)
df_deaths_new = converttable(df_deaths)


# In[4]:


# Change dates format
df_confirmed_new['dt']=pd.to_datetime(df_confirmed_new['dt'])
df_deaths_new['dt']=pd.to_datetime(df_deaths_new['dt'])


# In[5]:


# Rename cols
df_confirmed_new.rename(columns = {'value': 'confirmed'}, inplace = True)
df_deaths_new.rename(columns = {'value': 'deaths'}, inplace = True)


# In[6]:


# Merge two tables
df_merged = df_confirmed_new.merge(df_deaths_new[['Province/State', 'Country/Region', 'dt', 'deaths']], 
                                   on = ['Province/State', 'Country/Region', 'dt'], 
                                   how = 'inner')
df_merged = df_merged[['Province/State', 'Country/Region', 'Lat', 'Long', 'dt', 'confirmed', 'deaths']]
#df_merged.head()


# In[7]:


# Extract and aggregate data for countries with provinces

# US
#df_us = df_merged[df_merged['Country/Region'] == 'US'].copy()
#df_merged.drop(index = df_us.index, inplace = True)
#us_agg = df_us.groupby(by = 'dt').sum().copy()
#us_agg.reset_index(inplace = True)
#us_agg['Lat'] = 37.0902
#us_agg['Long'] = -95.7129
#us_agg['Province/State'] = np.nan
#us_agg['Country/Region'] = 'US'
#df_merged = pd.concat([df_merged, us_agg], sort = False, ignore_index = True)

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


# In[8]:


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

# Check
#df_merged[df_merged['Country/Region'] == 'Germany'][['dt', 'confirmed', 'deaths', 'days_since_1st_conf',
#                                                     'days_since_50th_conf', 'days_since_10th_deaths']]


# In[9]:


# Daily new cases (confirmed and deaths)

# Sort values
df_merged.sort_values(by = ['Country/Region', 'dt'], ascending = True, inplace = True)
# Differences
df_merged['confirmed_newcases'] = df_merged.groupby(by = ['Country/Region']).confirmed.diff()
df_merged['deaths_newcases'] = df_merged.groupby(by = ['Country/Region']).deaths.diff()
#df_merged[df_merged['Country/Region'] == 'Germany'][['dt', 'confirmed', 'confirmed_diff']]

# Moving average

# Create columns
df_merged['confirmed_newcases_movavg'] = np.nan
df_merged['deaths_newcases_movavg'] = np.nan
# Number of days
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


# In[10]:


# New cases growth (new cases today divided by new cases yesterday)

# Create columns
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


# In[11]:


# Open population table
df_pop = pd.read_csv('../data_tables/world_pop_by_country.csv')
df_pop.rename(columns = {'Country Name': 'Country/Region', '2018': 'population_2018'}, inplace = True)

# Merge population table
df_merged = df_merged.merge(df_pop, on = 'Country/Region', how = 'left')

#df_merged.sort_values('dt').head()


# In[12]:


# Cases by 100.000 hab.
df_merged['confirmed_by100000pop'] = df_merged['confirmed']*100000/df_merged['population_2018']
df_merged['deaths_by100000pop'] = df_merged['deaths']*100000/df_merged['population_2018']

# Drop intermediate columns
#df_merged.drop(columns = ['Country Code', 'population_2018'], inplace = True)
df_merged.drop(columns = ['Country Code'], inplace = True)


# In[13]:


# Mortality rate
df_merged['MortalityRate'] = df_merged['deaths']/df_merged['confirmed']


# In[14]:


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


# In[15]:


# Plotting colors
top10_col = ['#719949', '#FF6900', '#E8927C', '#A6192E', '#51284F', 
             '#A192B2', '#418FDE', '#86C8BC', '#286140', '#F1C400']

title_col = '#002D72'
subtitle_col = 'grey'
label_col = 'dimgray'
two_color_a = '#002D72'
two_color_b = '#009B77'

# Plotting fonts & sizes
title_font = 'Gentona, Tahoma, sans-serif'
subtitle_font = 'Gentona, Tahoma, sans-serif'
label_font = 'Gentona, Tahoma, sans-serif'
title_size = 24
subtitle_size = 18
label_size = 12
label_size_small = 8

# Graph sizes
width_px = 720
height_px = 450
width_px_small = 360
height_px_small = 275

# Line size
line_width = 2 

# Margins
margin_t = 20
margin_b = 150
margin_r = 20
margin_l = 50

# Ticks
tick_lenght = 12
tick_col = '#eee'


# ## <span style="color:orange">New cases</span>
# <hr style="border: 1px solid #D3D3D3" >

# In[16]:


# Select data for plotting

# Data for the top 10 countries in number of confirmed cases
last_date = df_merged['dt'].max()
top10 = df_merged[df_merged['dt'] == last_date].sort_values(by = 'deaths', ascending = False).iloc[0:10, :] 
top10_country = top10['Country/Region'].values


# In[17]:


# Plot new cases top 10 countries
data = []

for i, c in enumerate(top10_country):
    nc = df_merged[df_merged['Country/Region'] == c].confirmed_newcases_movavg
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = nc,
                           name = c+'  ',
                           marker = dict(color = top10_col[i]),
                           line = dict(width = line_width),
                           hoverinfo = 'text',
                           hovertext = [c+':<br>{:.0f}'.format(i) for i in nc],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                             bgcolor = 'white',
                                             font = dict(color = top10_col[i])),
                           showlegend = True
                          )
               )
    
    
lay = go.Layout(width = width_px, 
                height = height_px, 
                xaxis = dict(ticks = 'inside',
                             ticklen = tick_lenght,
                             tickcolor = tick_col,
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
                              y = -0.20,
                              orientation = 'h',
                             ),
                margin=dict(l = margin_l, r = margin_r, b = margin_b, t = margin_t, pad=0),
                annotations=[dict(x = 0.0,
                                  y = -0.20,
                                  showarrow = False,
                                  text = 'Click any country below to hide/show from the graph:',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = label_size,
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
out_file = open(path+'timeline_newcases_date_all_720.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[18]:


# Plot new cases top 10 countries 360px
data = []

for i, c in enumerate(top10_country):
    nc = df_merged[df_merged['Country/Region'] == c].confirmed_newcases_movavg
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = nc,
                           name = c+'  ',
                           marker = dict(color = top10_col[i]),
                           line = dict(width = 1.5),
                           hoverinfo = 'text',
                           hovertext = [c+':<br>{:.0f}'.format(i) for i in nc],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                             bgcolor = 'white',
                                             font = dict(color = top10_col[i])),
                           showlegend = True
                          )
               )
    
    
lay = go.Layout(width = 360, 
                height = 275, 
                #bargap = 0.2,
                xaxis = dict(#nticks = 10,
                             ticks = 'inside',
                             ticklen = 6,
                             tickcolor = '#eee',
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = False,
                            ),
                yaxis = dict(title='Confirmed new cases',
                             type = 'linear',
                            ),
                hovermode = 'closest',
                font = dict(size = label_size_small,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = -0.05, 
                              y = -0.22,
                              orientation = 'h',
                             ),
                margin=dict(l=30, r=10, b=0, t=10, pad=0),
                annotations=[dict(x = -0.03,
                                  y = -0.25,
                                  showarrow = False,
                                  text = 'Click any country below to hide/show from the graph:',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = label_size_small,
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
out_file = open(path+'timeline_newcases_date_all_360.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[19]:


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
                    xaxis = dict(#nticks = 10,
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
                    margin=dict(l=50, r=20, b=100, t=30, pad=0),
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


# In[20]:


# Data to JSON
most_recent_day = df_merged.sort_values('dt').dt.unique()[-3]
tmp = df_merged[ (df_merged['dt'] == most_recent_day) & (df_merged['Country/Region'].isin(top10_country))].copy()

def up_or_down(x):
    if (x>=1):
        return 'up'
    else:
        return 'down'

tmp['trend'] = tmp.apply(lambda x: up_or_down(x['confirmed_newcases_growth_movavg']), axis=1)
trend = tmp[['Country/Region', 'trend']].copy()

most_recent_day = df_merged.sort_values('dt').dt.unique()[-1]
tmp = df_merged[ (df_merged['dt'] == most_recent_day) & (df_merged['Country/Region'].isin(top10_country))].copy()
tmp.sort_values(by = 'deaths', ascending = False, inplace = True)
tmp = tmp[['Country/Region', 'days_since_1st_conf', 'first_confirmed', 
           'confirmed', 'deaths']]
tmp = tmp.merge(trend, on = 'Country/Region')
tmp['graph_number'] = np.arange(10)
tmp['last_update'] = pd.Timestamp.now(tz='US/Eastern')
tmp.set_index('Country/Region', inplace = True)
tmp.rename(columns={'Country/Region': 'country',
                    'first_confirmed': 'date_first_confirmed',
                   }, inplace = True)
path = '../visuals/new_cases/'
tmp.to_json(path+'country_info.json', orient = 'columns')

#tmp


# ## <span style="color:orange">Mortality rates</span>
# <hr style="border: 1px solid #D3D3D3" >
# 
# 

# In[21]:


# Plot mortality ratio

# Assign color to top10
top10['color'] = top10_col
bar_width = 0.6
bar_opacity = 0.6

# Plot

text_a = ['{:.1f}'.format(x)+'%' for x in top10.sort_values(by = 'MortalityRate')['MortalityRate']*100]
text_b = ['{:.2f}'.format(x) for x in top10.sort_values(by = 'deaths_by100000pop')['deaths_by100000pop']]
#text_a[-1] = f'Mortality: {text_a[-1]}'
#text_b[-1] = f'Mortality: {text_b[-1]}'
text_a[-1] = 'Mortality: '+text_a[-1]
text_b[-1] = 'Mortality: '+text_b[-1]

data = [go.Bar(x = top10.sort_values(by = 'MortalityRate')['MortalityRate']*100,
               y = top10.sort_values(by = 'MortalityRate')['Country/Region'],
               orientation = 'h',
               name = 'mort_conf',
               opacity = bar_opacity,
               marker = dict(color = '#FF9E1B'),
               hoverinfo = 'skip',
               hovertext = ['Mortality:<br>'+'{:.1f}'+'%'.format(x) for x in top10.sort_values(by = 'MortalityRate')['MortalityRate']*100],
               hoverlabel = dict(bordercolor = top10.sort_values(by = 'MortalityRate')['color'], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10.sort_values(by = 'MortalityRate')['color'])),
               text = text_a,
               textfont=dict(
                    color='black'
               ),
               textposition = 'auto',
               width = bar_width
              ),
        go.Bar(x = top10.sort_values(by = 'deaths_by100000pop')['deaths_by100000pop'],
               y = top10.sort_values(by = 'deaths_by100000pop')['Country/Region'],
               orientation = 'h',
               name = 'mort_pop',
               opacity = bar_opacity,
               marker = dict(color = '#FF9E1B'),
               hoverinfo = 'skip',
               hovertext = ['Mortality:<br>'+'{:.2f}'.format(x) for x in top10.sort_values(by = 'deaths_by100000pop')['deaths_by100000pop']],
               hoverlabel = dict(bordercolor = top10.sort_values(by = 'deaths_by100000pop')['color'], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10.sort_values(by = 'deaths_by100000pop')['color'])),
               text = text_b,
               textfont=dict(
                    color='black'
               ),
               textposition = 'auto',
               width = bar_width,
               visible = False,
              )
       ]

lay = go.Layout(width = width_px, 
                height = height_px,
                margin=dict(l=100, r=50, b=50, t=80, pad=4),
                plot_bgcolor='white',
                #bargap = 0.2,
                xaxis = dict(title='Mortality: Observed case-fatality ratio',
                             nticks = 10,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = True,
                             gridcolor = 'lightgray',
                             ticksuffix="%",
                            ),
                yaxis = dict(title='',
                             showgrid = False,
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 1.03, 
                              y = 0.7),
                updatemenus=[dict(
                                    type = "buttons",
                                    direction = "left",
                                    buttons=list([
                                        dict(args = [{'visible': [True, False]},
                                                     {'xaxis' : dict(title='Mortality: Observed case-fatality ratio',
                                                         nticks = 10,
                                                         rangemode = 'nonnegative',
                                                         zeroline = False,
                                                         showgrid = True,
                                                         gridcolor = 'lightgray',
                                                         ticksuffix="%",
                                                        )}],
                                                     label = 'Observed case-fatality ratio',
                                                     #method = 'restyle'
                                                     method = 'update'
                                                    ),
                                        dict(args = [{'visible': [False, True]},
                                                     {'xaxis' : dict(title='Mortality: Deaths per 100,000 population',
                                                         nticks = 10,
                                                         rangemode = 'nonnegative',
                                                         zeroline = False,
                                                         showgrid = True,
                                                         gridcolor = 'lightgray',
                                                         ticksuffix="",
                                                        )}],
                                                     label = 'Deaths per 100,000 population',
                                                     #method = 'restyle'
                                                     method = 'update'
                                                    )
                                               ]),
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x=0,
                                  xanchor="left",
                                  y=1.2,
                                  yanchor="top",
                                  bordercolor = 'lightgray'
                                 ),
                            ]
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
    
path = '../visuals/mortality/'
out_file = open(path+'mortality_top10_720.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[22]:


# Plot mortality ratio (mobile size)

# Assign color to top10
top10['color'] = top10_col
bar_width = 0.6
bar_opacity = 0.6

# Plot

text_a = ['{:.1f}'.format(x)+'%' for x in top10.sort_values(by = 'MortalityRate')['MortalityRate']*100]
text_b = ['{:.2f}'.format(x) for x in top10.sort_values(by = 'deaths_by100000pop')['deaths_by100000pop']]
#text_a[-1] = f'Mortality: {text_a[-1]}'
#text_b[-1] = f'Mortality: {text_b[-1]}'
text_a[-1] = 'Mortality: '+text_a[-1]
text_b[-1] = 'Mortality: '+text_b[-1]

data = [go.Bar(x = top10.sort_values(by = 'MortalityRate')['MortalityRate']*100,
               y = top10.sort_values(by = 'MortalityRate')['Country/Region'],
               orientation = 'h',
               name = 'mort_conf',
               opacity = bar_opacity,
               marker = dict(color = '#FF9E1B'),
               hoverinfo = 'skip',
               hovertext = ['Mortality:<br>'+'{:.1f}'+'%'.format(x) for x in top10.sort_values(by = 'MortalityRate')['MortalityRate']*100],
               hoverlabel = dict(bordercolor = top10.sort_values(by = 'MortalityRate')['color'], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10.sort_values(by = 'MortalityRate')['color'])),
               text = text_a,
               textfont=dict(color='black',
                            ),
               textposition = 'auto',
               width = bar_width
              ),
        go.Bar(x = top10.sort_values(by = 'deaths_by100000pop')['deaths_by100000pop'],
               y = top10.sort_values(by = 'deaths_by100000pop')['Country/Region'],
               orientation = 'h',
               name = 'mort_pop',
               opacity = bar_opacity,
               marker = dict(color = '#FF9E1B'),
               hoverinfo = 'skip',
               hovertext = ['Mortality:<br>'+'{:.2f}'.format(x) for x in top10.sort_values(by = 'deaths_by100000pop')['deaths_by100000pop']],
               hoverlabel = dict(bordercolor = top10.sort_values(by = 'deaths_by100000pop')['color'], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10.sort_values(by = 'deaths_by100000pop')['color'])),
               text = text_b,
               textfont=dict(
                    color='black'
               ),
               textposition = 'auto',
               width = bar_width,
               visible = False,
              )
       ]

lay = go.Layout(width = width_px_small, 
                height = height_px_small+80,
                margin=dict(l=100, r=50, b=50, t=100, pad=4),
                plot_bgcolor='white',
                #bargap = 0.2,
                xaxis = dict(title='Mortality: Observed case-fatality ratio',
                             nticks = 10,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = True,
                             gridcolor = 'lightgray',
                             ticksuffix="%",
                            ),
                yaxis = dict(title='',
                             showgrid = False,
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 1.03, 
                              y = 0.7),
                annotations=[dict(x = 0.02,
                                  y = 1.2,
                                  showarrow = False,
                                  text = '', #Mortality ratios for the most affected countries
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = title_font,
                                      size = title_size,
                                      color = title_col,),
                                 ),
                             dict(x = 0.02,
                                  y = 1.1,
                                  showarrow = False,
                                  text = '',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = subtitle_font,
                                      size = subtitle_size,
                                      color = subtitle_col,),
                                 ),
                             dict(x = 1.40,
                                  y = 0.95,
                                  showarrow = False,
                                  text = '',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = label_size_small,
                                      color = label_col,),
                             
                             )
                            ],
                updatemenus=[dict(
                                    type = "buttons",
                                    direction = "down",
                                    buttons=list([
                                        dict(args = [{'visible': [True, False]},
                                                     {'xaxis' : dict(title='Mortality: Observed case-fatality ratio',
                                                         nticks = 10,
                                                         rangemode = 'nonnegative',
                                                         zeroline = False,
                                                         showgrid = True,
                                                         gridcolor = 'lightgray',
                                                         ticksuffix="%",
                                                        )}],
                                                     label = 'Observed case-fatality ratio',
                                                     #method = 'restyle'
                                                     method = 'update'
                                                    ),
                                        dict(args = [{'visible': [False, True]},
                                                     {'xaxis' : dict(title='Mortality: Deaths per 100,000 population',
                                                         nticks = 10,
                                                         rangemode = 'nonnegative',
                                                         zeroline = False,
                                                         showgrid = True,
                                                         gridcolor = 'lightgray',
                                                         ticksuffix="",
                                                        )}],
                                                     label = 'Deaths per 100,000 population',
                                                     #method = 'restyle'
                                                     method = 'update'
                                                    )
                                               ]),
                                  pad = {"r": 10, "t": 0},
                                  showactive = True,
                                  x=0,
                                  xanchor="left",
                                  y=1.35,
                                  yanchor="top",
                                  bordercolor = 'lightgray'
                                 ),
                            ]
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
    
path = '../visuals/mortality/'
out_file = open(path+'mortality_top10_360.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[23]:


# Plot mortality rates

most_recent_day = df_merged.sort_values('dt').dt.unique()[-1]

filt = ((df_merged['dt'] == most_recent_day) & (df_merged['deaths'] > 2))
pattern = '|'.join(top10_country)
top10_df_merged = df_merged[(df_merged['Country/Region'].str.contains(pattern) & filt)]

# Plot
data = [go.Scatter(x = df_merged[filt]['confirmed'],
                   y = df_merged[filt]['deaths'],
                   marker = dict(color = 'orange', size = 6),
                   mode = 'markers',
                   hoverinfo = 'text',
                   hovertext = [y+':<br>'+'{:.1f}%'.format(x*100) for x,y in zip(df_merged[filt]['MortalityRate'], 
                                                                          df_merged[filt]['Country/Region'])],
                   hoverlabel = dict(bordercolor = 'gray',
                                     bgcolor = 'white',
                                     font = dict(color = 'gray')),
                   text = df_merged[filt]['Country/Region'],
                   textposition = "top center"
              ),
        go.Scatter(x = top10_df_merged['confirmed'],
                   y = top10_df_merged['deaths'],
                   marker = dict(color = 'orange', 
                                 size = 6,
                                 opacity = 1,
                                line=dict(
                                    color = 'black',
                                    width = 1,
                                )),
                   mode = 'markers',
                   hoverinfo = 'text',
                   hovertext = [y+':<br>'+'{:.1f}%'.format(x*100) for x,y in zip(top10_df_merged['MortalityRate'], 
                                                                          top10_df_merged['Country/Region'])],
                   hoverlabel = dict(bordercolor = 'gray',
                                     bgcolor = 'white',
                                     font = dict(color = 'gray')),
              ),
        go.Scatter(x = [0, 1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   y = [0, 0.1*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, 1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   y = [0, 0.05*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, 1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   y = [0, 0.02*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, 1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   y = [0, 0.01*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, 1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   y = [0, 0.005*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = df_merged[filt]['population_2018'],
                   y = df_merged[filt]['deaths'],
                   marker = dict(color = 'orange', size = 6),
                   mode = 'markers',
                   hoverinfo = 'text',
                   hovertext = [y+':<br>'+'{:.2f}'.format(x) for x,y in zip(df_merged[filt]['deaths_by100000pop'], 
                                                                          df_merged[filt]['Country/Region'])],
                   hoverlabel = dict(bordercolor = 'gray',
                                     bgcolor = 'white',
                                     font = dict(color = 'gray')),
                   visible = False,
                  ),
        go.Scatter(x = top10_df_merged['population_2018'],
                   y = top10_df_merged['deaths'],
                   marker = dict(color = 'orange', 
                                 size = 6,
                                 opacity = 1,
                                line=dict(
                                    color = 'black',
                                    width = 1,
                                )),
                   mode = 'markers',
                   hoverinfo = 'text',
                   hovertext = [y+':<br>'+'{:.2f}'.format(x) for x,y in zip(top10_df_merged['deaths_by100000pop'], 
                                                                          top10_df_merged['Country/Region'])],
                   hoverlabel = dict(bordercolor = 'gray',
                                     bgcolor = 'white',
                                     font = dict(color = 'gray')),
                   visible = False,
                  ),
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 100*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
        
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 10*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 1*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 0.1*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 0.01*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
       ]

annotations_titles = [dict(x = 0.02,
                           y = 1.2,
                           showarrow = False,
                           text = '', #Mortality ratios worldwide
                           xref = 'paper',
                           yref = 'paper',
                           font=dict(family = title_font,
                                     size = title_size,
                                     color = title_col,),
                          ),
                      dict(x = 0.02,
                           y = 1.1,
                           showarrow = False,
                           text = '',
                           xref = 'paper',
                           yref = 'paper',
                           font=dict(family = subtitle_font,
                                     size = subtitle_size,
                                     color = subtitle_col,),
                          ),
                      dict(x = 1.32,
                           y = 0.95,
                           showarrow = False,
                           text = '',
                           xref = 'paper',
                           yref = 'paper',
                           font=dict(family = label_font,
                                     size = label_size,
                                     color = label_col,),
                          )
                     ]

annotations_a = annotations_titles + [
    dict(x = np.log10(1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         y = np.log10(0.1*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -30,
         text = '10%',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         y = np.log10(0.05*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -30,
         text = '5%',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         y = np.log10(0.02*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -30,
         text = '2%',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         y = np.log10(0.01*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -30,
         text = '1%',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         y = np.log10(0.005*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -30,
         text = '0.5%',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        )]

annotations_b = annotations_titles + [
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(100*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         halign='right',
         height = 30,
         textangle = -21,
         text = ('100'+'<br>'+'per 100k population'),
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(10*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -21,
         text = '10',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(1*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -21,
         text = '1',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(0.1*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -21,
         text = '0.1',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(0.01*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -21,
         text = '0.01',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        )
]

visibility_a = [True, True, True, True, True, True, True, False, False, False, False, False, False, False]
visibility_b = [False, False, False, False, False, False, False, True, True, True, True, True, True, True]

lay = go.Layout(width = width_px, 
                height = height_px,
                margin=dict(l=60, r=50, b=50, t=80, pad=4),
                plot_bgcolor='white',
                xaxis = dict(title='Confirmed cases',
                             type = 'log',
                             dtick = 1,
                             ticks = 'outside',
                             ticklen = tick_lenght/2,
                             tickcolor = label_col,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showline=True,
                             linecolor = label_col,
                             showgrid = False,
                            ),
                yaxis = dict(title='Deaths',
                             type = 'log',
                             dtick = 1,
                             ticks = 'outside',
                             ticklen = tick_lenght/2,
                             tickcolor = label_col,
                             showgrid = False,
                             showline=True,
                             linecolor = label_col,
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 1.03, 
                              y = 0.7),
                showlegend = False,
                annotations= annotations_a,
                updatemenus=[dict(type = "buttons",
                                  direction = "left",
                                  buttons=list([dict(args = [{'visible': visibility_a},
                                                             {'xaxis.title': 'Confirmed cases',
                                                              'annotations': annotations_a,
                                                             }],
                                                     label = 'Observed case-fatality ratio',
                                                     method = 'update'
                                                    ),
                                                dict(args = [{'visible': visibility_b},
                                                             {'xaxis.title': 'Population',
                                                              'annotations': annotations_b,
                                                             }
                                                            ],
                                                     label = 'Deaths per 100,000 population',
                                                     method = 'update'
                                                    ),
                                               ]),
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x=0,
                                  xanchor="left",
                                  y=1.2,
                                  yanchor="top",
                                  bordercolor = 'lightgray',
                                 ),
                            ]
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
    
path = '../visuals/mortality/'
out_file = open(path+'mortality_all_720.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()

#df_merged[filt]['Lat'][69]
#coordinates = (df_merged[filt]['Lat'][69], df_merged[filt]['Long'][69]), (df_merged[filt]['Lat'][69], df_merged[filt]['Long'][69])
#reverse_geocode.search(coordinates)


# In[24]:


# Plot mortality rates

most_recent_day = df_merged.sort_values('dt').dt.unique()[-1]

filt = ((df_merged['dt'] == most_recent_day) & (df_merged['deaths'] > 2))
pattern = '|'.join(top10_country)
top10_df_merged = df_merged[(df_merged['Country/Region'].str.contains(pattern) & filt)]

# Plot
data = [go.Scatter(x = df_merged[filt]['confirmed'],
                   y = df_merged[filt]['deaths'],
                   marker = dict(color = 'orange', size = 6),
                   mode = 'markers',
                   hoverinfo = 'text',
                   hovertext = [y+':<br>'+'{:.1f}%'.format(x*100) for x,y in zip(df_merged[filt]['MortalityRate'], 
                                                                          df_merged[filt]['Country/Region'])],
                   hoverlabel = dict(bordercolor = 'gray',
                                     bgcolor = 'white',
                                     font = dict(color = 'gray')),
                   text = df_merged[filt]['Country/Region'],
                   textposition = "top center"
              ),
        go.Scatter(x = top10_df_merged['confirmed'],
                   y = top10_df_merged['deaths'],
                   marker = dict(color = 'orange', 
                                 size = 6,
                                 opacity = 1,
                                line=dict(
                                    color = 'black',
                                    width = 1,
                                )),
                   mode = 'markers',
                   hoverinfo = 'text',
                   hovertext = [y+':<br>'+'{:.1f}%'.format(x*100) for x,y in zip(top10_df_merged['MortalityRate'], 
                                                                          top10_df_merged['Country/Region'])],
                   hoverlabel = dict(bordercolor = 'gray',
                                     bgcolor = 'white',
                                     font = dict(color = 'gray')),
              ),
        go.Scatter(x = [0, 1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   y = [0, 0.1*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, 1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   y = [0, 0.02*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, 1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   y = [0, 0.005*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = df_merged[filt]['population_2018'],
                   y = df_merged[filt]['deaths'],
                   marker = dict(color = 'orange', size = 6),
                   mode = 'markers',
                   hoverinfo = 'text',
                   hovertext = [y+':<br>'+'{:.2f}'.format(x) for x,y in zip(df_merged[filt]['deaths_by100000pop'], 
                                                                          df_merged[filt]['Country/Region'])],
                   hoverlabel = dict(bordercolor = 'gray',
                                     bgcolor = 'white',
                                     font = dict(color = 'gray')),
                   visible = False,
                  ),
        go.Scatter(x = top10_df_merged['population_2018'],
                   y = top10_df_merged['deaths'],
                   marker = dict(color = 'orange', 
                                 size = 6,
                                 opacity = 1,
                                line=dict(
                                    color = 'black',
                                    width = 1,
                                )),
                   mode = 'markers',
                   hoverinfo = 'text',
                   hovertext = [y+':<br>'+'{:.2f}'.format(x) for x,y in zip(top10_df_merged['deaths_by100000pop'], 
                                                                          top10_df_merged['Country/Region'])],
                   hoverlabel = dict(bordercolor = 'gray',
                                     bgcolor = 'white',
                                     font = dict(color = 'gray')),
                   visible = False,
                  ),
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 100*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
        
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 10*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 1*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 0.1*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
        go.Scatter(x = [0, df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()],
                   y = [0, 0.01*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000],
                   marker = dict(color = 'gray'),
                   line = dict(width = 0.3),
                   mode = 'lines',
                   visible = False,
                   hoverinfo = 'skip',
              ),
       ]

annotations_titles = [dict(x = 0.02,
                           y = 1.2,
                           showarrow = False,
                           text = '', #Mortality ratios worldwide
                           xref = 'paper',
                           yref = 'paper',
                           font=dict(family = title_font,
                                     size = title_size,
                                     color = title_col,),
                          ),
                      dict(x = 0.02,
                           y = 1.1,
                           showarrow = False,
                           text = '',
                           xref = 'paper',
                           yref = 'paper',
                           font=dict(family = subtitle_font,
                                     size = subtitle_size,
                                     color = subtitle_col,),
                          ),
                      dict(x = 1.32,
                           y = 0.95,
                           showarrow = False,
                           text = '',
                           xref = 'paper',
                           yref = 'paper',
                           font=dict(family = label_font,
                                     size = label_size,
                                     color = label_col,),
                          )
                     ]

annotations_a = annotations_titles + [
    dict(x = np.log10(1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         y = np.log10(0.1*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -30,
         text = '10%',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         y = np.log10(0.02*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -30,
         text = '2%',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         y = np.log10(0.005*1.3*df_merged[df_merged['dt'] == most_recent_day]['confirmed'].max()),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -30,
         text = '0.5%',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        )]

annotations_b = annotations_titles + [
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(100*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         halign='right',
         height = 30,
         textangle = -21,
         text = ('100/100k pop'),
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(10*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -21,
         text = '10',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(1*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -21,
         text = '1',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(0.1*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -21,
         text = '0.1',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        ),
    dict(x = np.log10(df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()),
         y = np.log10(0.01*df_merged[df_merged['dt'] == most_recent_day]['population_2018'].max()/100000),
         showarrow = False,
         valign = 'top',
         height = 30,
         textangle = -21,
         text = '0.01',
         xref = 'x',
         yref = 'y',
         font=dict(family = label_font,
                   size = label_size,
                   color = label_col,),
        )
]

visibility_a = [True, True, True, True, True, False, False, False, False, False, False, False]
visibility_b = [False, False, False, False, False, True, True, True, True, True, True, True]

lay = go.Layout(width = width_px_small, 
                height = height_px_small,
                margin=dict(l=60, r=50, b=50, t=100, pad=4),
                plot_bgcolor='white',
                xaxis = dict(title='Confirmed cases',
                             type = 'log',
                             dtick = 1,
                             ticks = 'outside',
                             ticklen = tick_lenght/2,
                             tickcolor = label_col,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showline=True,
                             linecolor = label_col,
                             showgrid = False,
                            ),
                yaxis = dict(title='Deaths',
                             type = 'log',
                             dtick = 1,
                             ticks = 'outside',
                             ticklen = tick_lenght/2,
                             tickcolor = label_col,
                             showgrid = False,
                             showline=True,
                             linecolor = label_col,
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 1.03, 
                              y = 0.7),
                showlegend = False,
                annotations= annotations_a,
                updatemenus=[dict(type = "buttons",
                                  direction = "down",
                                  buttons=list([dict(args = [{'visible': visibility_a},
                                                             {'xaxis.title': 'Confirmed cases',
                                                              'annotations': annotations_a,
                                                             }],
                                                     label = 'Observed case-fatality ratio',
                                                     method = 'update'
                                                    ),
                                                dict(args = [{'visible': visibility_b},
                                                             {'xaxis.title': 'Population',
                                                              'annotations': annotations_b,
                                                             }
                                                            ],
                                                     label = 'Deaths per 100,000 population',
                                                     method = 'update'
                                                    ),
                                               ]),
                                  pad = {"r": 10, "t": 0},
                                  showactive = True,
                                  x=0,
                                  xanchor="left",
                                  y=1.6,
                                  yanchor="top",
                                  bordercolor = 'lightgray',
                                 ),
                            ]
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
    
path = '../visuals/mortality/'
out_file = open(path+'mortality_all_360.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()

#df_merged[filt]['Lat'][69]
#coordinates = (df_merged[filt]['Lat'][69], df_merged[filt]['Long'][69]), (df_merged[filt]['Lat'][69], df_merged[filt]['Long'][69])
#reverse_geocode.search(coordinates)


# In[25]:


# Table with data
most_recent_day = df_merged.sort_values('dt').dt.unique()[-1]
tmp = df_merged[(df_merged['dt'] == most_recent_day) & (df_merged['deaths']>2)].sort_values('deaths', ascending = False).copy()
tmp = tmp[['Country/Region', 'confirmed', 'deaths', 'MortalityRate', 'deaths_by100000pop']]
tmp.rename(columns={'Country/Region': 'Country',
                    'confirmed': 'Confirmed',
                    'deaths': 'Deaths',
                    'MortalityRate': 'Case-Fatality',
                    'deaths_by100000pop': 'Deaths/100k pop.',
                   }, inplace = True)

tmp.sort_values('Deaths', ascending = False, inplace=True)
tmp['Case-Fatality'] = ['{:.1f}%'.format(x) for x in tmp['Case-Fatality']*100]
tmp['Deaths/100k pop.'] = ['{:.2f}'.format(x) for x in tmp['Deaths/100k pop.']]
tmp['Confirmed'] = ['{:,}'.format(x) for x in tmp['Confirmed']]
tmp['Deaths'] = ['{:,}'.format(x) for x in tmp['Deaths']]

tmp.reset_index(drop=True, inplace = True)

path = '../visuals/mortality/'
tmp.to_json(path+'table.json', orient = 'columns')
#tmp.head()
#tmp.shape[0]


# ## <span style="color:orange">Timelines</span>
# <hr style="border: 1px solid #D3D3D3" >
# 
# 

# In[26]:


df_merged.head()


# In[27]:


# Plot timeline confirmed top ten countries

# Plot

data = []
for i, c in enumerate(top10_country):
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].deaths,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].deaths_by100000pop,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths_by100000pop],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))

conf_visible = [True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False]
death_visible = [False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False]
conf_pop_visible = [False, False, True, False, False, False, True, False, False, False, True, False,
                    False, False, True, False, False, False, True, False, False, False, True, False, 
                    False, False, True, False, False, False, True, False, False, False, True, False, 
                    False, False, True, False]
death_pop_visible = [False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True]

lay = go.Layout(width = width_px, 
                height = height_px, 
                xaxis = dict(title='',
                             ticks = 'inside',
                             ticklen = tick_lenght-3,
                             tickcolor = tick_col,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = False,
                            ),
                yaxis = dict(title='Number of Cases',
                             type = 'linear',
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 0.0, 
                              y = -0.23,
                              orientation = 'h',
                             ),
                margin=dict(l = margin_l, r = margin_r, b = margin_b, t = margin_t, pad=0),
                annotations=[dict(x = 0.0,
                                  y = -0.25,
                                  showarrow = False,
                                  text = 'Click any country below to hide/show from the graph:',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = label_size,
                                      color = 'silver',),
                                 ),
                            ],
                updatemenus=[dict(buttons=list([dict(args = ["yaxis.type", 'linear'],
                                                     label = 'Linear',
                                                     method = 'relayout'
                                                    ),
                                                dict(
                                                    args = ["yaxis.type", 'log'],
                                                    label = 'Logarithmic',
                                                    method = 'relayout'
                                                )
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.265,
                                  xanchor = 'left',
                                  y = 1.2,
                                  yanchor = 'top'
                                 ),
                             dict(buttons=list([dict(args = [{'visible': conf_visible, 'showlegend' : True }],
                                                     label = 'Confirmed   ',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_visible, 'showlegend' : True }],
                                                     label = 'Deaths',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': conf_pop_visible, 'showlegend' : True }],
                                                     label = 'Confirmed/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_pop_visible, 'showlegend' : True }],
                                                     label = 'Deaths/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.02,
                                  xanchor = 'left',
                                  y = 1.2,
                                  yanchor = 'top'
                                 ),
                            ]
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

path = '../visuals/timelines/'
out_file = open(path+'timeline_date_720.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[39]:


# Plot timeline confirmed top ten countries (360)

# Plot

data = []
for i, c in enumerate(top10_country):
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].deaths,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].deaths_by100000pop,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths_by100000pop],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))

conf_visible = [True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False]
death_visible = [False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False]
conf_pop_visible = [False, False, True, False, False, False, True, False, False, False, True, False,
                    False, False, True, False, False, False, True, False, False, False, True, False, 
                    False, False, True, False, False, False, True, False, False, False, True, False, 
                    False, False, True, False]
death_pop_visible = [False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True]

lay = go.Layout(width = width_px_small-23, 
                height = height_px_small+100, 
                xaxis = dict(title='',
                             ticks = 'inside',
                             ticklen = tick_lenght-3,
                             tickcolor = tick_col,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = False,
                            ),
                yaxis = dict(title='Number of Cases',
                             type = 'linear',
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 0.0, 
                              y = -0.40,
                              orientation = 'h',
                             ),
                margin=dict(l = 50, r = 10, b = 10, t = 65, pad=0),
                annotations=[dict(x = 0.0,
                                  y = -0.45,
                                  showarrow = False,
                                  text = 'Click any country below to hide/show from the graph:',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = label_size,
                                      color = 'silver',),
                                 ),
                            ],
                updatemenus=[dict(buttons=list([dict(args = ["yaxis.type", 'linear'],
                                                     label = 'Linear',
                                                     method = 'relayout'
                                                    ),
                                                dict(
                                                    args = ["yaxis.type", 'log'],
                                                    label = 'Logarithmic',
                                                    method = 'relayout'
                                                )
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.6,
                                  xanchor = 'left',
                                  y = 1.35,
                                  yanchor = 'top'
                                 ),
                             dict(buttons=list([dict(args = [{'visible': conf_visible, 'showlegend' : True }],
                                                     label = 'Confirmed   ',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_visible, 'showlegend' : True }],
                                                     label = 'Deaths',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': conf_pop_visible, 'showlegend' : True }],
                                                     label = 'Confirmed/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_pop_visible, 'showlegend' : True }],
                                                     label = 'Deaths/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.02,
                                  xanchor = 'left',
                                  y = 1.35,
                                  yanchor = 'top'
                                 ),
                            ]
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

path = '../visuals/timelines/'
out_file = open(path+'timeline_date_360.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[29]:


# Plot timeline confirmed top ten countries

# Plot

data = []
for i, c in enumerate(top10_country):
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].days_since_50th_conf,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].days_since_50th_conf,
                           y = df_merged[df_merged['Country/Region'] == c].deaths,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].days_since_50th_conf,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].days_since_50th_conf,
                           y = df_merged[df_merged['Country/Region'] == c].deaths_by100000pop,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths_by100000pop],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))

conf_visible = [True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False]
death_visible = [False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False]
conf_pop_visible = [False, False, True, False, False, False, True, False, False, False, True, False,
                    False, False, True, False, False, False, True, False, False, False, True, False, 
                    False, False, True, False, False, False, True, False, False, False, True, False, 
                    False, False, True, False]
death_pop_visible = [False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True]

lay = go.Layout(width = width_px, 
                height = height_px, 
                #bargap = 0.2,
                xaxis = dict(title='Days since 50th case confirmed',
                             ticks = 'inside',
                             ticklen = tick_lenght-3,
                             tickcolor = tick_col,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = False,
                            ),
                yaxis = dict(title='Number of Cases',
                             type = 'linear',
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 0.0, 
                              y = -0.33,
                              orientation = 'h',
                             ),
                margin=dict(l = margin_l, r = margin_r, b = margin_b, t = margin_t, pad=0),
                annotations=[dict(x = 0.0,
                                  y = -0.35,
                                  showarrow = False,
                                  text = 'Click any country below to hide/show from the graph:',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = label_size,
                                      color = 'silver',),
                                 ),
                            ],
                updatemenus=[dict(buttons=list([dict(args = ["yaxis.type", 'linear'],
                                                     label = 'Linear',
                                                     method = 'relayout'
                                                    ),
                                                dict(
                                                    args = ["yaxis.type", 'log'],
                                                    label = 'Logarithmic',
                                                    method = 'relayout'
                                                )
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.265,
                                  xanchor = 'left',
                                  y = 1.2,
                                  yanchor = 'top'
                                 ),
                             dict(buttons=list([dict(args = [{'visible': conf_visible, 'showlegend' : True }],
                                                     label = 'Confirmed   ',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_visible, 'showlegend' : True }],
                                                     label = 'Deaths',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': conf_pop_visible, 'showlegend' : True }],
                                                     label = 'Confirmed/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_pop_visible, 'showlegend' : True }],
                                                     label = 'Deaths/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.02,
                                  xanchor = 'left',
                                  y = 1.2,
                                  yanchor = 'top'
                                 ),
                            ]
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

path = '../visuals/timelines/'
out_file = open(path+'timeline_days_720.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[38]:


# Plot timeline confirmed top ten countries (360)

# Plot

data = []
for i, c in enumerate(top10_country):
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].days_since_50th_conf,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           line = dict(width = 1.5),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].days_since_50th_conf,
                           y = df_merged[df_merged['Country/Region'] == c].deaths,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           line = dict(width = 1.5),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].days_since_50th_conf,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           line = dict(width = 1.5),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].days_since_50th_conf,
                           y = df_merged[df_merged['Country/Region'] == c].deaths_by100000pop,
                           name = c,
                           marker = dict(color = top10_col[i]),
                           line = dict(width = 1.5),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths_by100000pop],
                           hoverlabel = dict(bordercolor = top10_col[i], 
                                 bgcolor = 'white', 
                                 font = dict(color = top10_col[i])),
                           showlegend = False,
                           visible = False
                          ))

conf_visible = [True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False, True, False, False, False, True, False, False, False,
                True, False, False, False]
death_visible = [False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False, False, True, False, False, False, True, False, False, 
                 False, True, False, False]
conf_pop_visible = [False, False, True, False, False, False, True, False, False, False, True, False,
                    False, False, True, False, False, False, True, False, False, False, True, False, 
                    False, False, True, False, False, False, True, False, False, False, True, False, 
                    False, False, True, False]
death_pop_visible = [False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True, False, False, False, True, False, False, False, True, 
                      False, False, False, True]

lay = go.Layout(width = width_px_small-23, 
                height = height_px_small+100, 
                #bargap = 0.2,
                xaxis = dict(title='',
                             ticks = 'inside',
                             ticklen = tick_lenght-3,
                             tickcolor = tick_col,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = False,
                            ),
                yaxis = dict(title='Number of Cases',
                             type = 'linear',
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                legend = dict(x = 0.0, 
                              y = -0.45,
                              orientation = 'h',
                             ),
                margin=dict(l = 50, r = 10, b = 10, t = 60, pad=0),
                annotations=[dict(x = 0.0,
                                  y = -0.50,
                                  showarrow = False,
                                  text = 'Click any country below to hide/show from the graph:',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = label_size,
                                      color = 'silver',),
                                 ),
                             dict(x = 0.5,
                                  y = -0.3,
                                  showarrow = False,
                                  text = 'Days since 50th case confirmed',
                                  xref = 'paper',
                                  yref = 'paper',
                                  font=dict(
                                      family = label_font,
                                      size = label_size+2,
                                      color = label_col,),
                                 ),
                            ],
                updatemenus=[dict(buttons=list([dict(args = ["yaxis.type", 'linear'],
                                                     label = 'Linear',
                                                     method = 'relayout'
                                                    ),
                                                dict(
                                                    args = ["yaxis.type", 'log'],
                                                    label = 'Logarithmic',
                                                    method = 'relayout'
                                                )
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.6,
                                  xanchor = 'left',
                                  y = 1.35,
                                  yanchor = 'top'
                                 ),
                             dict(buttons=list([dict(args = [{'visible': conf_visible, 'showlegend' : True }],
                                                     label = 'Confirmed   ',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_visible, 'showlegend' : True }],
                                                     label = 'Deaths',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': conf_pop_visible, 'showlegend' : True }],
                                                     label = 'Confirmed/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_pop_visible, 'showlegend' : True }],
                                                     label = 'Deaths/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.02,
                                  xanchor = 'left',
                                  y = 1.35,
                                  yanchor = 'top'
                                 ),
                            ]
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

path = '../visuals/timelines/'
out_file = open(path+'timeline_days_360.html', 'w')
out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
out_file.write(plot)
out_file.write('</body><html>')
out_file.close()


# In[37]:


# Individual timeline country plots

for i, c in enumerate(top10_country):
    
    data = []
    
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed,
                           name = c,
                           marker = dict(color = '#FF9E1B'),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed],
                           hoverlabel = dict(bordercolor = 'gray', 
                                 bgcolor = 'white', 
                                 font = dict(color = 'gray')),
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].deaths,
                           name = c,
                           marker = dict(color = '#FF9E1B'),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:,}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths],
                           hoverlabel = dict(bordercolor = 'gray', 
                                 bgcolor = 'white', 
                                 font = dict(color = 'gray')),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop,
                           name = c,
                           marker = dict(color = '#FF9E1B'),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].confirmed_by100000pop],
                           hoverlabel = dict(bordercolor = 'gray', 
                                 bgcolor = 'white', 
                                 font = dict(color = 'gray')),
                           showlegend = False,
                           visible = False
                          ))
    data.append(go.Scatter(x = df_merged[df_merged['Country/Region'] == c].dt,
                           y = df_merged[df_merged['Country/Region'] == c].deaths_by100000pop,
                           name = c,
                           marker = dict(color = '#FF9E1B'),
                           hoverinfo = 'text',
                           hovertext = [c+'<br>'+'{:.1f}'.format(x) for x in df_merged[df_merged['Country/Region'] == c].deaths_by100000pop],
                           hoverlabel = dict(bordercolor = 'gray', 
                                 bgcolor = 'white', 
                                 font = dict(color = 'gray')),
                           showlegend = False,
                           visible = False
                          ))
    
    conf_visible = [True, False, False, False]
    death_visible = [False, True, False, False]
    conf_pop_visible = [False, False, True, False]
    death_pop_visible = [False, False, False, True]
    
    lay = go.Layout(width = width_px_small-23, 
                height = 360, 
                xaxis = dict(title='',
                             ticks = 'inside',
                             ticklen = tick_lenght-3,
                             tickcolor = tick_col,
                             rangemode = 'nonnegative',
                             zeroline = False,
                             showgrid = False,
                            ),
                yaxis = dict(title='Number of Cases',
                             type = 'linear',
                            ),
                hovermode = 'closest',
                font = dict(size = label_size,
                            family = label_font,
                            color = label_col,
                           ),
                showlegend = False,
                margin=dict(l = 50, r = 10, b = 50, t = 65, pad=0),
                updatemenus=[dict(buttons=list([dict(args = ["yaxis.type", 'linear'],
                                                     label = 'Linear',
                                                     method = 'relayout'
                                                    ),
                                                dict(
                                                    args = ["yaxis.type", 'log'],
                                                    label = 'Logarithmic',
                                                    method = 'relayout'
                                                )
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.6,
                                  xanchor = 'left',
                                  y = 1.17,
                                  yanchor = 'top',
                                 ),
                             dict(buttons=list([dict(args = [{'visible': conf_visible, 'showlegend' : True }],
                                                     label = 'Confirmed   ',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_visible, 'showlegend' : True }],
                                                     label = 'Deaths',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': conf_pop_visible, 'showlegend' : True }],
                                                     label = 'Confirmed/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                                dict(args = [{'visible': death_pop_visible, 'showlegend' : True }],
                                                     label = 'Deaths/100k pop.',
                                                     method = 'restyle'
                                                    ),
                                               ]),
                                  direction = "down",
                                  pad = {"r": 10, "t": 10},
                                  showactive = True,
                                  x = 0.02,
                                  xanchor = 'left',
                                  y = 1.17,
                                  yanchor = 'top'
                                 ),
                            ]
               )
    
    fig = dict(data=data, layout=lay)
    
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
    
    path = '../visuals/timelines/'
    out_file = open(path+'timeline_date_'+str(i)+'.html', 'w')
    out_file.write('<!DOCTYPE html><html><head><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head><body>')
    out_file.write(plot)
    out_file.write('</body><html>')
    out_file.close()

#plotly.offline.iplot(fig)


# In[32]:


# Data to JSON
most_recent_day = df_merged.sort_values('dt').dt.unique()[-1]
tmp = df_merged[ (df_merged['dt'] == most_recent_day) & (df_merged['Country/Region'].isin(top10_country))].copy()
tmp.sort_values(by = 'deaths', ascending = False, inplace = True)
tmp = tmp[['Country/Region', 'days_since_1st_conf', 'first_confirmed', 
           'confirmed_newcases', 'deaths_newcases']]
tmp['graph_number'] = np.arange(10)
tmp.set_index('Country/Region', inplace = True)
tmp.rename(columns={'Country/Region': 'country',
                    'first_confirmed': 'date_first_confirmed',
                   }, inplace = True)
path = '../visuals/timelines/'
tmp.to_json(path+'country_info.json', orient = 'columns')

#tmp

