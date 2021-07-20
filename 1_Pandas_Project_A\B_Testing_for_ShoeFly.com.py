import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(10))


most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(most_views)

ad_clicks['is_click'] = ~(ad_clicks.ad_click_timestamp.isnull())
print(ad_clicks.head(10))

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns = 'is_click', values = 'user_id', index = 'utm_source')

clicks_pivot['percent_clicked'] = (clicks_pivot[True]
/ (clicks_pivot[False]+clicks_pivot[True])) * 100
print(clicks_pivot)

most_views = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(most_views)

A_or_B = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
print(A_or_B)

a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A'].reset_index()
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B'].reset_index()
print(a_clicks,b_clicks)
percent_by_day_a = a_clicks.groupby('day').user_id.count().reset_index()
percent_by_day_b = b_clicks.groupby('day').user_id.count().reset_index()
print(percent_by_day_a,percent_by_day_b)

better_add = percent_by_day_a['user_id'] - percent_by_day_b['user_id']
print(better_add)
