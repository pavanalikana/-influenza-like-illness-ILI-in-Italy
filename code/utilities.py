
def toCapitalize(str):
    str = str[:1].upper() + str[1:]
    return str

#This function retrieves the views of the Wikipedia page <pagename> from the pageview API 
def retrieve_pageviews(pagename):  
    # We are considering below time period as per the data that we have from Influnet survivelence system,
    # Which is for better correlation
    
    from_ = "20151012"
    to_ = "20180429"
    wiki_page =  pd.DataFrame(index = range((datetime.datetime.strptime(to_, "%Y%m%d").date() - datetime.datetime.strptime(from_, "%Y%m%d").date()).days), columns=["date", "views"])
    try:
        cont = 0
        for v in pageviewapi.per_article('it.wikipedia', pagename, from_, to_, access='all-access', agent='all-agents', granularity='daily')["items"]:
            wiki_page.loc[cont] = [datetime.datetime.strptime(v["timestamp"][:-2], "%Y%m%d"), v["views"]]
            cont+=1
        wiki_page = wiki_page.set_index("date").resample('W').sum().reset_index()
        wiki_page["week"] = 0
        wiki_page["year"] = 0
        for i in range(len(wiki_page)):
            wiki_page.loc[i,"week"] = wiki_page.loc[i,"date"].isocalendar()[1]
            wiki_page.loc[i,"year"] = wiki_page.loc[i,"date"].isocalendar()[0]
        return(wiki_page)
    except pageviewapi.client.ZeroOrDataNotLoadedException:
        print("Page Not Found!!!" + pagename + "!!!")
    return []