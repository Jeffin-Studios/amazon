from googlesearch import search
import pytrends
from pytrends.request import TrendReq


def google_trends(search):

        # Set up the trend fetching object
        pytrends = TrendReq(hl='en-US', tz=360)
        kw_list = [search]
        
        # Create the search object
        pytrends.build_payload(kw_list, cat=0, geo='', gprop='news')
        
        # Get the interest over time
        interest = pytrends.interest_over_time()
        print(interest.head())

        # Get related searches
        related_queries = pytrends.related_queries()
        print(related_queries)

  #       # Get Google Top Charts
		# top_charts_df = pytrend.top_charts(cid='actors', date=201611)
		# print(top_charts_df.head())
        
        return interest, related_queries
  

if __name__ == '__main__':
	query = "gloves"
	for result in search(query, tld="co.in", num=10, stop=1, pause=2): 
	    print(result) 
	google_trends(query)



# Determines if source is credible and recent. Discards those that do not meet criteria
# def filter():


# from googlesearch.googlesearch import GoogleSearch
# response = GoogleSearch().search("NIO Stock Rating")
# for result in response.results:
#     print("Title: " + result.title)
#     print("Content: " + result.getText())