from broad_factual_information import TypeOne
import spacy


"""This recognises and processes individual queries. The reason why we take whole episodes is because the episode 
not only contains the relevant query we want to process but also it contains events that occurred before this one that 
can help Larity understand exactly what we've been talking about so far."""

nlp = spacy.load("en_core_web_sm")

def run(episode):


    #noun list will


    #create a dictionary for words that would map to certain commands. ex: "no" then maybe we got an error.


    #if first_query != 1:
    if episode.no_of_events = 1:
        #treat this as a first time juicer

    else:
        if episode.no_of_queries > 1:
            # check how long since the last query, if little time then do some error handling
            # check if error handling is online look for words like "no wait", "no" and time has to be little, "not" and we had another query right before this.

            # check last actions/reply/query\
            # things to extra: last actions that we did, the topic we are on
            # check last few queries for topic and noun extraction, how do ai chatbots work???





  #  text = query.information

    #-----------------ASR step-----------------#
    # Azure stuff

    #----------------------------------Classification----------------------------------#

    # pre-spacy classification:
    # check if we are currently in a query
    # check for any meta queries?
    #check if its a conversational prompt.?  like if its very short and small and its not a follow up.
    # what is a follow up? A follow up needs to be within like 0-5 seconds?

    # spacy classification_model

    # simple question checker for typeII (If its a small question that requires a straight answer) IIB
    # check if we are looking for an anecdote for typeIIC
    #trend_checker if we are in a type II
    # keyterms
   # juicer = TypeOne(text)
    #if juicer.has_proper_noun():  # for any proper nouns we need to go for trend checks
     #   pass
    #smaller trend checker for forums an niche online spaces IID and IIE



    # political/moral/heavy topic checker for type III (IIIA)
    # career advice/life advice checker IIIB
    # check if we are looking for summary reviews topics for Type III. specific product or tvshow or whatever IIIC

    #education_checker for type IV? If we need to explain a concept


    # -----------------Clarification & Speech Synthesis -----------------#


    # -----------------SERP Scraper and general scraping-----------------#

    # wikipedia scraping

    # -----------------NLP Analysis of Scrape results-----------------#

    # -----------------Speech Synthesis-----------------#






    return


if __name__ == '__main__':

    run("yo this is amazing")
