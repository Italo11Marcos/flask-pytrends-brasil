from pytrends.request import TrendReq
pytrend = TrendReq()


def google_trends():
    trends_brazil = list()
    trending_searches_df = pytrend.trending_searches(pn='brazil')
    #print(trending_searches_df.head(10))
    trends_list = trending_searches_df.head(10).values.tolist()
    for trends in trends_list:
        trend = str(trends)
        trend = trend.replace("'","")
        trend = trend.replace("[", "")
        trend = trend.replace("]", "")
        trends_brazil.append(trend)
    return trends_brazil

