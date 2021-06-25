# Written Analysis of Mission-to-Mars

## Overview of Project
The objective of Mission-to-Mars is to use python functions and refactored indexes to scrape a particular website to return titles, photos, and URLs in a structured way. The website in question is https://marshemispheres.com/ which will be accessed through Jupyter Notebook functions such as BeautifulSoup and Splinter. A localized Mongo database will retain the information we will need such as the full url, and photographs of the four different martian hemispheres. Eventually the web app will also be altered to fit onto mobile screens and given its own personalizations. 

**Source of Data** : https://marshemispheres.com/

**Software** : Python 3.7.6 , Jupyter Notebook, Visual Studio Code, HTML/CSS.
## Results and Summary

### Titles and Image URLs
Through web scraping the base website, the location of titles and image URLs were determined and stored on a dictionary in Jupyter Notebook named hemisphere_image_urls. 
![Deliverable1](https://user-images.githubusercontent.com/82983000/123373767-f5562f00-d553-11eb-938a-c4dd6e5089cb.png)

### Updated Web App
The Web app was updated to include titles and full resolution images of all four martian hemispheres, the updated code is found in scraping.py and index(1) in the templates folder. 
![Deliverable2Mars](https://user-images.githubusercontent.com/82983000/123373891-34848000-d554-11eb-9cf6-6f9d5b79cffc.png)

### Bootstrap 3 Components
The index(1) HTML file was once again refactored to make the web app suitable for mobile use and some personalization. The web app would run on any mobile device as indicated in the first image, which is run on an IPad Pro.
![Deliberable 3](https://user-images.githubusercontent.com/82983000/123374136-a8bf2380-d554-11eb-883e-120b3f1f97d1.png)

Further personalizations were added through the change of the background color from white to orange, in solidarity towards the martian theme. The “Scrape New Data” button was also highlighted to give a better contrast as the white letters were more tedious to read on a light blue background to another white background. 
![Deliberable 3 backround color and scrape new data stylized](https://user-images.githubusercontent.com/82983000/123374363-05bad980-d555-11eb-8b94-6f5f70cee0eb.png)


