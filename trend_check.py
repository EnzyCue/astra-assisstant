from constants import TREND_CHECK_DIFFERENCE, OLD_TIME, CURRENT_TIME
from pytrends.request import TrendReq

#Note: the dataframes returned by pytrends here contain 5 Spacy_Neural_Network_Data points for the allocated time point.


def is_trending(term):  # Accepts string and gives bolean if its trending right now on or not (relative to 3 months ago)

    current_trend_mean = get_trend_mean(term, CURRENT_TIME)
    old_trend_mean = get_trend_mean(term, OLD_TIME)

    if current_trend_mean - old_trend_mean > TREND_CHECK_DIFFERENCE:
        print(f"{current_trend_mean} - {old_trend_mean} = {current_trend_mean - old_trend_mean}")
        return True

    return False


def get_trend_mean(term, time):
    search_term = [term] # they only accept lists for the payload I think

    trend = TrendReq(hl='en-US', tz=10) #language and time zone
    trend.build_payload(search_term, cat=0, timeframe=time) #cat = 0 means no specified category
    trend_df = trend.interest_over_time()  # the dataframe of date, trend score and ispartial(irrelevant)
    return trend_df[term].mean()



