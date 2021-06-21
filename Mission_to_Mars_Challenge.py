#!/usr/bin/env python
# coding: utf-8

# In[98]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[99]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[100]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[101]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[102]:


slide_elem.find('div', class_='content_title')


# In[103]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[104]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images 

# In[105]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[106]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[107]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[108]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[109]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[110]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[111]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles 
# 

# In[112]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[138]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# click on the link to get the high def image, then click sample to get the real one, thats the one we want
# Using a for loop, iterate through the tags or CSS element.

#for item range len()  (THIS DOESNT WORK)


for j in range(4):
    #hmake the thing 
    hemisphere = {}
    #run the for function with j
    #browser.find_by_css('a.product-item h1')[j].click()
    #browser.find_by_css('a.product-item h2')[j].click()
    browser.find_by_css('a.product-item h3')[j].click()
    
    element = browser.links.find_by_text('Sample').first

    img_url = element['href']
    #s
    hemisphere['img_url'] = img_url
    
    
    
    #find the title usint hemi['title']
    
    title = browser.find_by_css('h2.title').text
    
    hemisphere['title'] = title
    
    hemisphere_image_urls.append(hemisphere)
    #for the hemisphere image, and d) use browser.back() to navigate back to the beginning to get the next hemisphere image.
    browser.back()








# In[139]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[140]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:




