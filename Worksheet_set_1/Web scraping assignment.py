#!/usr/bin/env python
# coding: utf-8

# # WEB SCRAPING Assignment
# 

# In all the following questions, you have to use BeautifulSoup to scrape different websites and collect data as per 
# the requirement of the question.
# 

# Print Data Frame in every Answers of the questions
# 

# Use Jupyter Notebooks to program, upload it on your GitHub and send the link of the jupyter notebook to your 
# SME.
# 

# 1. Write a python program to display all the header tags from‘en.wikipedia.org/wiki/Main_Page’.
# 

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page.content
soup = BeautifulSoup(page.content, "html.parser")
titles = soup.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# In[9]:


page.status_code


# In[3]:


all_headers=[]
for i in range(0,len(titles)):
    all_headers.append(titles[i].get_text().replace("\n"," "))
all_headers


# In[2]:


import pandas as pd


# In[16]:


df=pd.DataFrame(all_headers)
df


# In[17]:


len(df)


# 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of release).
# 

# In[19]:


page=requests.get("https://www.imdb.com/chart/top/")


# In[20]:


page


# In[21]:


soup=BeautifulSoup(page.content,"html.parser")
soup


# In[22]:


print(soup.prettify())


# In[23]:


#top 100 movies name
name=soup.find_all("td",class_="titleColumn")
name


# In[24]:


movies_name=[]
for i in name:
    movies_name.append(i.text.replace("\n",""))
movies_name


# In[25]:


movies_name=[]
for i in name:
    for j in i.find_all("a"):
        movies_name.append(j.text.replace("\n",""))
movies_name


# In[45]:


# top 100 rating of movies
rating=soup.find_all("td",class_="ratingColumn imdbRating")
rating


# In[46]:


imdb_rating=[]
for i in range(0,len(rating)):
    imdb_rating.append(rating[i].get_text().replace("\n"," "))
imdb_rating


# In[47]:


df=pd.DataFrame(imdb_rating)
df


# In[ ]:





# In[48]:


#top 100 movies year
year=soup.find_all("span",class_="secondaryInfo")
year


# In[55]:


imdb_year=[]
for i in range(0,len(year)):
    imdb_year.append(year[i].get_text().replace("\n",""))
imdb_year                    


# In[56]:


df=pd.DataFrame(imdb_year)
df


# In[58]:


import pandas as pd
imdb_movies=pd.DataFrame({})
imdb_movies['movies_name']=movies_name[:100]
imdb_movies['imdb_rating']=imdb_rating[:100]
imdb_movies['imdb_year']=imdb_year[:100]
imdb_movies


# In[59]:


len(imdb_movies)


# 3.Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Yearof release).
# 

# In[60]:


page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=RFWHP8EJXW87APTKVXZT&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_hd ")


# In[61]:


page


# In[62]:


soup=BeautifulSoup(page.content)
soup


# In[63]:


print(soup.prettify())


# In[64]:


#top 100 indian movies name
name=soup.find_all("td",class_="titleColumn")
name


# In[65]:


movies_name=[]
for i in name:
    movies_name.append(i.text.replace("\n",""))
movies_name


# In[66]:


movies_name=[]
for i in name:
    for j in i.find_all("a"):
        movies_name.append(j.text.replace("\n",""))
movies_name


# In[67]:


#top 100 indian ratings movies
rating=soup.find_all("td",class_="ratingColumn imdbRating")


# In[69]:


rating


# In[70]:


imdb_rating=[]
for i in range(0,len(rating)):
    imdb_rating.append(rating[i].get_text().replace("\n",""))
imdb_rating


# In[71]:


df=pd.DataFrame(imdb_rating)
df


# In[31]:


#top 100 indian movies year
year=soup.find_all("span",class_="secondaryInfo")
year


# In[72]:


imdb_year=[]
for i in range(0,len(year)):
    imdb_year.append(year[i].get_text().replace("\n",""))
imdb_rating


# In[74]:


df=pd.DataFrame(imdb_rating)
df


# In[78]:


indian_movies=pd.DataFrame({})
indian_movies['movies_name']=movies_name[0:100]
indian_movies['movies_ratings']=imdb_rating[0:100]
indian_movies["movies_year"]=imdb_year[0:100]
indian_movies


# In[ ]:





# In[35]:


len(indian_movies)


# 4. Write a python program to scrap book name, author name, genre and book review of any 5 books from‘www.bookpage.com’
# 
# 

# In[213]:


page=requests.get("https://bookpage.com/reviews/26593-winfred-rembert-chasing-me-to-my-grave-nonfiction#.YSEBeflR1PY")
page


# In[214]:


soup=BeautifulSoup(page.content)
soup


# In[215]:


print(soup.prettify())


# In[250]:


book_name=soup.find("h1",class_="italic")
book_name


# In[251]:


book_name1=book_name.text.replace("\n","")
book_name1


# In[ ]:





# In[253]:


author_name=soup.find("h4",class_="sans")
author_name


# In[254]:


author_name1=author_name.text.replace("\n","")
author_name1


# In[260]:


genre=soup.find("p",class_="genre-links")
genre


# In[261]:


genre1=genre.text.replace("\n","")
genre1


# In[267]:


book_review=soup.find("div",class_="content-well article-show")
book_review


# In[268]:


book_review1=book_review.text.replace("\n","")
book_review1


# In[ ]:





# In[225]:


page=requests.get("https://bookpage.com/reviews/26469-derek-b-miller-how-to-find-your-way-dark-fiction#.YSD3iflR1PY")
page


# In[226]:


soup=BeautifulSoup(page.content)
soup


# In[49]:


print(soup.prettify)


# In[50]:


book_name=soup.find("h1",class_="italic")
book_name


# In[51]:


book_name.text.replace("\n","")


# In[52]:


author_name=soup.find("h4",class_="sans")
author_name


# In[53]:


author_name.text.replace("\n","")


# In[54]:


genre=soup.find("p",class_="genre-links")
genre


# In[55]:


genre.text.replace("\n","")


# In[56]:


book_review=soup.find("div",class_="article-body")
book_review


# In[57]:


book_review.text.replace("\n","")


# In[58]:


page=requests.get("https://bookpage.com/reviews/26490-rodrigo-garcia-farewell-to-gabo-mercedes-nonfiction#.YSEHg_lR1PY")
page


# In[59]:


soup=BeautifulSoup(page.content)
soup


# In[60]:


print(soup.prettify)


# In[61]:


book_name=soup.find("h1",class_="italic")
book_name


# In[62]:


book_name.text.replace("\n","")


# In[63]:


author_name=soup.find("h4",class_="sans")
author_name


# In[64]:


author_name.text.replace("\n","")


# In[65]:


genre=soup.find("p",class_="genre-links")
genre


# In[66]:


genre.text.replace("\n","")


# In[67]:


book_review=soup.find("div",class_="article-body")
book_review


# In[68]:


book_review.text.replace("\n","")


# In[69]:


page=requests.get("https://bookpage.com/reviews/26377-jason-mott-hell-book-fiction#.YSEK_flR1PY")
page


# In[70]:


soup=BeautifulSoup(page.content)
soup


# In[71]:


print(soup.prettify)


# In[72]:


book_name=soup.find("h1",class_="italic")
book_name


# In[73]:


book_name.text.replace("\n","")


# In[74]:


author_name=soup.find("h4",class_="sans")
author_name


# In[75]:


author_name.text.replace("\n","")


# In[76]:


genre=soup.find("p",class_="genre-links")
genre


# In[77]:


genre.text.replace("\n","")


# In[78]:


book_review=soup.find("div",class_="article-body")
book_review


# In[79]:


book_review.text.replace("\n","")


# In[80]:


page=requests.get("https://bookpage.com/features/26522-i-hate-how-much-i-love-you-romance#.YSENtPlR1PY")
page


# In[81]:


soup=BeautifulSoup(page.content)
soup


# In[82]:


print(soup.prettify)


# In[83]:


book_name=soup.find("h1",class_="italic")
book_name


# In[84]:


book_name.text.replace("\n","")


# In[85]:


author_name=soup.find("p",class_="sans bold author-info")
author_name


# In[86]:


author_name.text.replace("\n"," ")


# In[87]:


genre=soup.find("p",class_="genre-links sans")
genre


# In[88]:


genre.text.replace("\n","")


# In[89]:


book_review=soup.find("div",class_="article-body")
book_review


# In[90]:


book_review.text.replace("\n","")

5. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:
i) Top 10 ODI teams in men’s cricket along with the records for matches, points andrating.

# In[91]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[92]:


soup=BeautifulSoup(page.text,"lxml")
soup


# In[93]:


table=soup.find("table",class_="table")
table


# In[94]:


headers=[]
for i in table.find_all("th"):
    title=i.text.replace("\n","").strip()
    headers.append(title)


# In[95]:


df= pd.DataFrame(columns= headers)
df


# In[96]:


for row in table.find_all('tr')[1:]:
    data=row.find_all("td")
    row_data=[td.text.replace("\n","").strip() for td in data]
    length=len(df)
    df.loc[length]=row_data
    #df.to_csv("row_data")


# In[97]:


df=pd.read_csv("top_teams_data")
df


# In[ ]:





# In[98]:


df=pd.DataFrame(data=df,columns=headers)
df.head(10)


# ii) Top 10 ODI Batsmen in men along with the records of their team and rating.
# 

# In[99]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page


# In[100]:


soup=BeautifulSoup(page.text,"lxml")
soup


# In[101]:


table=soup.find("table",class_="table rankings-table")
table


# In[102]:


headers=[]
for i in table.find_all("th"):
    title=i.text.replace("\n"," ").strip()
    headers.append(title)


# In[103]:


df= pd.DataFrame(columns= headers)
df


# In[104]:


for row in table.find_all('tr')[1:]:
    data=row.find_all("td")
    row_data=[td.text.replace("\n","").strip() for td in data]
    length=len(df)
    df.loc[length]=row_data
    #df.to_csv("top_batsmen_data")


# In[105]:


df=pd.read_csv("top_batsmen_data")
df


# In[106]:


df=pd.DataFrame(data=df,columns=headers)
df.head(10)


# iii) Top 10 ODI bowlers along with the records of their team and rating.
# 

# In[107]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page


# In[108]:


soup=BeautifulSoup(page.text,"lxml")
soup


# In[109]:


table=soup.find("table",class_="table rankings-table")
table


# In[110]:


headers=[]
for i in table.find_all("th"):
    title=i.text.replace("\n"," ").strip()
    headers.append(title)


# In[111]:


df=pd.DataFrame(columns= headers)
df


# In[112]:


for row in table.find_all('tr')[1:]:
    data=row.find_all("td")
    row_data=[td.text.replace("\n","").strip() for td in data]
    length=len(df)
    df.loc[length]=row_data
    #df.to_csv("top_bowlers_data")


# In[113]:


df=pd.read_csv("top_bowlers_data")
df


# In[114]:


df=pd.DataFrame(data=df,columns=headers)
df.head(10)


# 6. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have toscrape:
# 

# i) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# 

# In[115]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[116]:


soup=BeautifulSoup(page.text,"lxml")
soup


# In[117]:


table=soup.find("table",class_="table")
table


# In[118]:


headers=[]
for i in table.find_all("th"):
    title=i.text.replace("\n"," ").strip()
    headers.append(title)


# In[119]:


df=pd.DataFrame(columns=headers)
df


# In[120]:


for row in table.find_all('tr')[1:]:
    data=row.find_all("td")
    row_data=[td.text.replace("\n","").strip() for td in data]
    length=len(df)
    df.loc[length]=row_data
    df.to_csv("top_teams_womens_cricket")


# In[121]:


df=pd.read_csv("top_teams_womens_cricket")
df


# In[122]:


df=pd.DataFrame(data=df,columns=headers)
df


# ii) Top 10 women’s ODI players along with the records of their team and rating.
# 

# In[123]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page


# In[124]:


soup=BeautifulSoup(page.text,"lxml")
soup


# In[125]:


table=soup.find("table",class_="table rankings-table")
table


# In[126]:


headers=[]
for i in table.find_all("th"):
    title=i.text.replace("\n"," ").strip()
    headers.append(title)


# In[127]:


df=pd.DataFrame(columns=headers)
df


# In[128]:


for row in table.find_all('tr')[1:]:
    data=row.find_all("td")
    row_data=[td.text.replace("\n","").strip() for td in data]
    length=len(df)
    df.loc[length]=row_data
    #df.to_csv("top_players_womens_teams")


# In[129]:


df=pd.read_csv("top_players_womens_teams")
df


# In[130]:


df=pd.DataFrame(data=df,columns=headers)
df.head(10)


# iii) Top 10 women’s ODI all-rounder along with the records of their team and rating.
# 

# In[131]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page


# In[132]:


soup=BeautifulSoup(page.text,"lxml")
soup


# In[133]:


table=soup.find("table",class_="table rankings-table")
table


# In[134]:


headers=[]
for i in table.find_all("th"):
    title=i.text.replace("\n"," ").strip()
    headers.append(title)


# In[135]:


df=pd.DataFrame(columns=headers)
df


# In[136]:


for row in table.find_all('tr')[1:]:
    data=row.find_all("td")
    row_data=[td.text.replace("\n","").strip() for td in data]
    length=len(df)
    df.loc[length]=row_data
    #df.to_csv("top_odi_allrounders_womens")


# In[137]:


df=pd.read_csv("top_odi_allrounders_womens")
df


# In[138]:


df=pd.DataFrame(data=df,columns=headers)
df.head(10)


# 7. Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The 
# scraped data should include Product Name, Price, Image URL and Average Rating.
# 

# In[20]:


page=requests.get("https://www.amazon.in/Mobile-Phone-Under-20000-Rupees/s?k=Mobile+Phone+Under+20000+Rupees")
page


# In[21]:


soup=BeautifulSoup(page.content,"lxml")
soup


# In[22]:


names=soup.find_all("h2",class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
names


# In[23]:


mobile_name=[]
for i in range(0,len(names)):
    mobile_name.append(names[i].get_text())
mobile_name


# In[24]:


len("mobile_name")


# In[ ]:





# In[25]:


prices=soup.find_all("span",class_="a-offscreen")
prices


# In[ ]:





# In[26]:


mobile_price=[]
for i in range(0,len(prices)):
    mobile_price.append(prices[i].get_text())
mobile_price


# In[27]:


len(mobile_price)


# In[28]:


my_list=(mobile_price)
my_list=list(dict.fromkeys(my_list))
print(my_list)


# In[ ]:





# In[29]:


mobile_price=pd.DataFrame(my_list)
mobile_price


# In[ ]:





# In[30]:


mobile_url=[]
x=soup.find_all("img",class_="s-image")
for img in x:
    mobile_url.append(img["src"])
mobile_url


# In[31]:


len(mobile_url)


# In[ ]:





# In[32]:


images=soup.find_all("img",class_="s-image")

for image in images:
    name=image["alt"]
    link=image["src"]
    print(link)


# In[ ]:





# In[33]:


rating=soup.find_all("span",class_="a-icon-alt")
rating


# In[34]:


mobile_rate=[]
for i in range(0,len(rating)):
    mobile_rate.append(rating[i].get_text())
mobile_rate


# In[35]:


mobile_rate.reverse()


# In[36]:


mobile_rate


# In[37]:


mobile_rate.pop(0)


# In[38]:


mobile_rate.pop(0)


# In[39]:


mobile_rate.pop(0)


# In[40]:


mobile_rate.pop(0)


# In[41]:


len(mobile_rate)


# In[42]:


mobile_rate.sort()


# In[43]:


mobile_rate


# In[ ]:





# In[44]:


import pandas as pd
import csv


# In[47]:


details_mobiles_phones=pd.DataFrame({})
details_mobiles_phones['mobile_name']=mobile_name
details_mobiles_phones['mobile_price']=mobile_price
details_mobiles_phones["mobile_url"]=mobile_url
details_mobiles_phones['mobile_rate']=mobile_rate
details_mobiles_phones


# In[49]:


df=pd.DataFrame(details_mobiles_phones)
df.to_csv("details_mobiles_phones")


# In[50]:


df=pd.read_csv("details_mobiles_phones")
df


# 8. Write a python program to extract information about the local weather from the National Weather Service 
# website of USA, https://www.weather.gov/ for the city, San Francisco. You need to extract data about 7 day 
# extended forecast display for the city. The data should include period, short description, temperature and 
# description.
# 

# In[120]:


page=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YSeKfEvitPY")
page                  


# In[122]:


soup=BeautifulSoup(page.content,"html.parser")
soup


# In[123]:


period=soup.find_all("p",class_="period-name")
period


# In[124]:


period_name=[]
for i in range(0,len(period)):
    period_name.append(period[i].get_text().replace("\n",""))
period_name


# In[125]:


description=soup.find_all("p",class_="short-desc")
description


# In[126]:


short_description=[]
for i in range(0,len(description)):
    short_description.append(description[i].get_text().replace("\n",""))
short_description


# In[159]:


temp_high=soup.find_all("p",class_="temp temp-high")
temp_high


# In[160]:


temperature_high=[]
for i in range(0,len(temp_high)):
    temperature_high.append(temp_high[i].get_text().replace("\n",""))
temperature_high


# In[161]:


temp_low=soup.find_all("p",class_="temp temp-low")
temp_low


# In[162]:


temperature_low=[]
for i in range(0,len(temp_low)):
    temperature_low.append(temp_low[i].get_text().replace("\n",""))
temperature_low


# In[163]:


temperature_high.insert(1,'Low: 57 °F')


# In[164]:


temperature_high.insert(3,'Low: 57 °F')


# In[165]:


temperature_high.insert(5,'Low: 58 °F')


# In[166]:


temperature_high.insert(7,'Low: 56 °F')


# In[205]:


temp_data=temperature_high
temp_data


# In[187]:


desc_odd=soup.find_all("div",class_="row row-odd row-forecast")
desc_odd


# In[189]:


description_odd=[]
for i in range(0,len(desc_odd)):
    description_odd.append(desc_odd[i].get_text().replace("\n"," "))
description_odd


# In[190]:


desc_even=soup.find_all("div",class_="row row-even row-forecast")
desc_even


# In[191]:


description_even=[]
for i in range(0,len(desc_even)):
    description_even.append(desc_even[i].get_text().replace("\n"," "))
description_even


# In[192]:


description_odd.insert(1,'TonightIncreasing clouds, with a low around 57. West wind 13 to 18 mph decreasing to 6 to 11 mph after midnight. Winds could gust as high as 23 mph.'
)


# In[193]:


description_odd.insert(3, 'Friday NightWidespread haze before 9pm. Mostly clear, with a low around 57. Southwest wind 16 to 21 mph decreasing to 6 to 11 mph after midnight. Winds could gust as high as 26 mph.'
)


# In[194]:


description_odd.insert(5, 'Saturday NightMostly clear, with a low around 58. Breezy.'
)


# In[195]:


description_odd.insert(7, 'Sunday NightPartly cloudy, with a low around 56.'
)


# In[196]:


description_odd.insert(9, 'Monday NightMostly clear, with a low around 54.'
)


# In[197]:


description_odd.insert(11, 'Tuesday NightMostly clear, with a low around 54.'
)


# In[206]:


desc_data=description_odd
desc_data


# In[210]:


df=pd.DataFrame(description_odd)
df


# In[211]:


detailed_forecast=pd.DataFrame({})
detailed_forecast['period_name']=period_name
detailed_forecast['short_description']=short_description
detailed_forecast['temp_data']=temp_data
detailed_forecast['desc_data']=desc_data[:9]
detailed_forecast


# In[ ]:





# 9. Write a python program to scrape fresher job listings from ‘https://internshala.com/’. It should include job title, 
# company name, CTC, and apply date.
# 

# In[299]:


page=requests.get("https://internshala.com/fresher-jobs")
page


# In[300]:


soup=BeautifulSoup(page.content,"lxml")
soup


# In[301]:


title=soup.find_all("div",class_="heading_4_5 profile")
title


# In[302]:


job_title=[]
for i in range(0,len(title)):
    job_title.append(title[i].get_text().replace("\n"," "))
job_title


# In[303]:


import pandas as pd
df=pd.DataFrame(job_title)
df


# In[ ]:





# In[304]:


name=soup.find_all("div",class_="heading_6 company_name")
name


# In[305]:


company_name=[]
for i in range(0,len(name)):
    company_name.append(name[i].get_text().replace("\n",""))
company_name


# In[306]:


import pandas as pd
df=pd.DataFrame(company_name)
df


# In[329]:


ctc=soup.find_all("div",class_="item_body")                
ctc


# In[324]:


company_ctc=[]
for i in range(0,len(ctc)):
        company_ctc.append(ctc[i].get_text().replace("\n",""))
company_ctc


# In[325]:


import pandas as pd


# In[332]:


df= pd.DataFrame(company_ctc)
df


# In[313]:


import csv
company_details=pd.DataFrame({})


# In[314]:


company_details['job_title']=job_title
company_details['company_name']=company_name
company_details


# 10. Write a python program to scrape house details from https://www.nobroker.in/ for any location. It should 
# include house title, location, area, emi and price

# In[96]:


from csv import writer


# In[58]:


page=requests.get("https://www.nobroker.in/property/sale/pune/multiple?searchParam=W3sibGF0IjoxOC41MzYyMDg0LCJsb24iOjczLjg5Mzk3NDgsInBsYWNlSWQiOiJDaElKZFJJcU9FN0F3anNSOHM4dDRUdnV5QjQiLCJwbGFjZU5hbWUiOiJLb3JlZ2FvbiBQYXJrIn0seyJsYXQiOjE4LjU2NzkxNDYsImxvbiI6NzMuOTE0MzQzMTk5OTk5OTksInBsYWNlSWQiOiJDaElKdFlRVTVrYkJ3anNSc0xPMHFQY3NTTFkiLCJwbGFjZU5hbWUiOiJWaW1hbiBOYWdhciJ9LHsibGF0IjoxOC41NDg4MTYxLCJsb24iOjczLjkyODE5NDksInBsYWNlSWQiOiJDaElKMVR5UTZXVEJ3anNSOUJpMDhvM19WMDgiLCJwbGFjZU5hbWUiOiJXYWRlc2h3YXIgTmFnYXIifV0=&radius=2.0&type=BHK2,BHK3,BHK4,BHK4PLUS&propertyAge=0")
page


# In[59]:


soup=BeautifulSoup(page.content,"html.parser")
soup


# In[60]:


title=soup.find_all("h2",class_="heading-6 font-semi-bold nb__1AShY")
title


# In[61]:


house_title=[]
for i in range(0,len(title)):
    house_title.append(title[i].get_text().replace("\n",""))
house_title


# In[62]:


location=soup.find_all("div",class_="nb__2CMjv")
location


# In[63]:


house_location=[]
for i in range(0,len(location)):
    house_location.append(location[i].get_text().replace("\n",""))
house_location


# In[64]:


area=soup.find_all("div",class_="nb__3oNyC")
area


# In[65]:


house_area=[]
for i in range(0,len(area)):
    house_area.append(area[i].get_text().replace("\n"," "))
house_area


# In[66]:


emi=soup.find_all("div",class_="font-semi-bold heading-6",id="roomType")
emi


# In[67]:


house_emi=[]
for i in range(0,len(emi)):
    house_emi.append(emi[i].get_text().replace("\n",""))
house_emi


# In[76]:


price=soup.find_all("div",class_="nb__2NPHR",id="minDeposit")
price


# In[79]:


house_price=[]
for i in range(0,len(price)):
    house_price.append(price[i].get_text().replace("\n"," "))
house_price


# In[ ]:





# In[80]:


import pandas as pd
house_details=pd.DataFrame({})
house_details['house_title']=house_title
house_details['house_location']=house_location
house_details['house_area']=house_area
house_details['house_emi']=house_emi
house_details['house_price']=house_price
house_details


# In[ ]:




