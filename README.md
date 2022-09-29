![hacktoberfest-white-banner](https://user-images.githubusercontent.com/89788120/192966740-a50f9b66-fe74-4899-a353-4459a0e37371.png)

### This project is now open to contributions under hacktoberfest 2022 and your contributions are welcome !


# RealTime-TwitterDataAnalysis
Collect and process real time twitter data to analyse popularity of tweets with specific keywords or hashtags , visualize important metrics, generate twitter networks and map tweets and trends geographically.

<br/>


**Analysing Twitter Data Can be useful in a wide variety of fields like:**

- In the industry it can be used in **Marketing and Product Analysis** to improve upon an organization's business decisions. 
- It can be used to **Measure public opinions** which can serve to gauge mood of people in important topics of interest such as political or social events. 
- Further , it can be used for **Clustering Behavioral Groups** by identifying conversation spheres , patterns in behaviour of diferent subsections of the society and also the bridges or major influencers.

<br>
<br/>
<br/>


- **Show Real Time Plot Of Tweet Volumes and Propotion Of the tweets mentioning either keyword**
<br/><br/>

![Total Volume Of tweets](https://i.postimg.cc/rsy2C9md/total-mentions.png)               ----              ![Average Mentions](https://i.postimg.cc/c1TS1P9f/average-mention.png)


<br/><br/>

- **Graph tweet sentiment by performing NLP**
<br/><br/>

![Tweet Sentriment](https://i.postimg.cc/HnSDS7c6/tweets-sentiment.png) 

<br/><br/>

- **Node Networks for Retweets And Replied Tweets  | Force Directed Circular Layout Showing more Retweeted user Larger in Size**

<br/><br/>


<div style = "margin-left: 500rem;">
<img alt = "node-network.png" src = "https://i.postimg.cc/Wz1xJbWg/node-network.png" style = " width : 20vw; left : 10vw; padding-left: 50px;" >&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img alt = "Circular-layout-reply-network" src = "https://i.postimg.cc/QxtrFSww/circular-network.png" style = "width : 24vw; ;" >
 
 </div>

<br/><br/>


### **Functionality**
- Stream tweets containing specific keywords in real time
- Show volume metrics for selected tweets in real time
- Filter tweeets by any time window
- Plot the prevalance of tweets regarding a particular topic of interest.
- Perform Sentiment analysis of tweets based on keyword and chart them in real time
- Twitter Networks Graphing follow , favorited , retweet and reply networks.
- Analyse Twitter Networks and discover important nodes that are influencers or conversation bridges.
- Display Tweets Geographically on a Map.

<br>

### Domains

- Data Mining
- Data Manipulation and Feature Engineering
- Big Data Analytics
- Natural Language Processing
- API and Web Server Communication
- Network Analysis

<br>


### Tech Stack

- tweepy
- nltk
- networkx
- streamlit
- pandas,numpy
- matplotlib

<br>
</br>

## Setup Locally

- Go the the cloned directory on your local machine.
- Run `pip install -r requirements.txt` to install all the dependencies.
- Get your Twitter API credentials and replace the placeholders in twitter_config.py.
- run `python main.py` which is the application entry point.

<br>

### Data Format

The data recieved from twitter stream api is in a json format

### Important Module and Object Structures

  **The Overall Structure Of the Project**
  [![twitter-Info-Structure.png](https://i.postimg.cc/6p8wmzhn/twitter-Info-Structure.png)](https://postimg.cc/gxbfwVQ2)

<!-- ### References and Important concepts For Analysis -->

## How to get started with contributions

- Read The [Contributing Guidelines](./Contributions.md) and [Code Of Conduct](./Code_Of_Conduct.md)

#### Steps To Contribute

- Fork this Repository.
- Clone the Repository: `git clone "url of this repo"`
- Check existing issues or raise a new issue of your own and ask it to be assigned to you.
- Wait for the issue to be assigned to you.
- Create a branch: `git checkout -b <your-new-branch-name>`
- Put your code :-

  - Make all necessary changes or modifications to the code in your local cloned branch.
  - Neccessary information like functionalities, screenshots, working video(if required) should be kept handy (you will need to present it when submitting the PR)

- Push changes to gitHub ( on your forked repo ) : `git push origin <add-your-branch-name>`
- Create a new pull request to the original repo ( main branch of this repo )
- Submit your changes for review.
- And Boom! You're done 🥳
- The maintainers will review and merge your changes into the main branch of this project. You will be automatically notified via E-mail once the changes have been merged.

#### Note : If you want your changes to count towards hacktoberfest ensure that the issue you are working on has #hacktoberfest label

---
