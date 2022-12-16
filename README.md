<!--
### This project is now open to contributions under hacktoberfest 2022 and your contributions are welcome.

#### To get started with contributing and the flow check out 👉 **[below](https://github.com/kaustav202/RealTime-TwitterDataAnalysis#how-to-get-started-with-contributions)**. This repo follows all the standard measures and compliances to ensure a healthy environment for collaboration and community engagement. 

How can you contribute ?

- [x] Check out the existing issues and help solve those or create a new one.
- [x] Report a bug or vulnerability in the project that needs to be corrected.
- [x] Any issue that may be a hinderance in normal working of the app.
- [x] Help with low-code and no-code like documentaion, the set-up and configuration, walkthrough.
- [x] Add new awesome features of your own without breaking existing ones.

Finally, let's relish the spirit of open source and have fun while bringing quality changes. Happy Contributing 🎉🎉 !!

-->

---

# RealTime-TwitterDataAnalysis
Collect and process real time twitter data to analyse popularity of tweets with specific keywords or hashtags , visualize important metrics, generate twitter networks and map tweets and trends geographically.

<br/>


**Analysing Twitter Data Can be useful in a wide variety of fields like:**

- In the industry it can be used in **Marketing and Product Analysis** to improve upon an organization's business decisions. 
- It can be used to **Measure public opinions** which can serve to gauge mood of people in important topics of interest such as political or social events. 
- Further , it can be used for **Clustering Behavioral Groups** by identifying conversation spheres , patterns in behaviour of diferent subsections of the society and also the bridges or major influencers.

<br/>
<br/>
<br/>


- **Show Real Time Plot Of Tweet Volumes and Proportion Of tweets mentioning either keyword**
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
- Filter tweets by any time window
- Plot the prevalance of tweets regarding a particular topic of interest.
- Perform Sentiment analysis of tweets based on keyword and chart them in real time
- Twitter Networks Graphing follow , favorited , retweet and reply networks.
- Analyse Twitter Networks and discover important nodes that are influencers or conversation bridges.
- Display Tweets Geographically on a Map.

</br>

### Domains
[![Badge](https://shields.io/badge/-Data--Mining-CAF4F4?logo=appveyor&logoColor=FF5733)]()&nbsp;
[![Badge](https://shields.io/badge/-Data--Manipulatio--and--Feature--Engineering-FCFFE9?logo=appveyor&logoColor=FF5733)]()&nbsp;
[![Badge](https://shields.io/badge/-Big--Data--Analytics-FFF2CC?logo=appveyor&logoColor=FF5733)]()&nbsp;
[![Badge](https://shields.io/badge/-Natural--Language--Processing-FDE0D9?logo=appveyor&logoColor=FF5733)]()&nbsp;
[![Badge](https://shields.io/badge/-API--and--Web--Server--Communication-CAEFD1?logo=appveyor&logoColor=FF5733)]()&nbsp;
[![Badge](https://shields.io/badge/-Network--Analysis-D3EEDD?logo=appveyor&logoColor=FF5733)]()

</br>


### Tech Stack
[![Badge](https://img.shields.io/badge/Streamlit-EE4C2C?style=for-the-badge&logo=streamlit&logoColor=white)]()&nbsp;
[![Badge](https://img.shields.io/badge/tweepy-1DA1F2?style=for-the-badge&logo=tweepy&logoColor=white)]()&nbsp;
[![Badge](https://img.shields.io/badge/nltk-000000?style=for-the-badge&logo=nltk&logoColor=white)]()&nbsp;
[![Badge](https://img.shields.io/badge/NetworkX-FFA500?style=for-the-badge&logo=NetworkX&logoColor=white)]()&nbsp;
[![Badge](https://img.shields.io/badge/pandas-035a7d?style=for-the-badge&logo=pandas&logoColor=white)]()&nbsp;
[![Badge](https://img.shields.io/badge/numpy-306998?style=for-the-badge&logo=numpy&logoColor=white)]()&nbsp;
[![Badge](https://img.shields.io/badge/matplotlib-FFC0CB?style=for-the-badge&logo=matplotlib&logoColor=white)]()

</br>
</br>

## Setup Locally

- Clone the repository on your local machine.
  ```sh
  git clone https://github.com/kaustav202/RealTime-TwitterDataAnalysis.git
  ```
- Go into the cloned directory
- Run `pip install -r requirements.txt` to install all the dependencies.
- Create a developer account on twitter: https://developer.twitter.com/en
- Get your Twitter API credentials and replace the placeholders in twitter_config.py.
    - Go to the Twitter Developer Portal Projects & Apps page at https://developer.twitter.com/en/portal/projects-and-apps
    - Find the API/consumer key and secret under the Consumer Keys section of the Keys and Tokens tab of your app
    - Your account's access token and secret for your app can be found under the Authentication Tokens section of the Keys and Tokens tab of your app
- From inside the `app/` folder, you can run `python stream.py` which adds(streams) the tweets into `tweets.json`
- Run `python main.py` which is the application entry point preferably after some time so that you have more tweets to perform the analysis.
- You can also perform Sentiment Analysis by running `python sentiment_analysis.py` and draw tweet network graphs by running `python tweet_network.py`
- Remember that the streaming (writing) of tweets is a completely independent step that needs to be performed initially by running stream.py

</br>

### Data Format

The data recieved from twitter stream api is in a json format

### Important Module and Object Structures

  **The Overall Structure Of the Project**
  [![twitter-Info-Structure.png](https://i.postimg.cc/6p8wmzhn/twitter-Info-Structure.png)](https://postimg.cc/gxbfwVQ2)

<!-- ### References and Important concepts For Analysis -->

## How to get started with contributions

- Read The [Contributing Guidelines](./Contributions.md) and [Code Of Conduct](./Code_Of_Conduct.md).

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

![GitHub release](https://img.shields.io/github/release/kaustav202/RealTime-TwitterDataAnalysis)</br>

![GitHub pull-requests merged](https://badgen.net/github/merged-prs/kaustav202/RealTime-TwitterDataAnalysis)&nbsp; &nbsp;![GitHub branches](https://badgen.net/github/branches/kaustav202/RealTime-TwitterDataAnalysis)&nbsp;&nbsp;![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) &nbsp; &nbsp; ![Maintainer](https://img.shields.io/badge/maintainer-Kaustav-blue)&nbsp; &nbsp;![GitHub license](https://badgen.net/github/license/kaustav202/RealTime-TwitterDataAnalysis)

![GitHub forks](https://badgen.net/github/forks/kaustav202/RealTime-TwitterDataAnalysis)&nbsp;&nbsp;![GitHub stars](https://badgen.net/github/stars/kaustav202/RealTime-TwitterDataAnalysis)&nbsp;&nbsp;![GitHub issues](https://img.shields.io/github/issues/kaustav202/RealTime-TwitterDataAnalysis)&nbsp;&nbsp;![GitHub contributors](https://img.shields.io/github/contributors/kaustav202/RealTime-TwitterDataAnalysis)


# Contributors 📑

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 120.0; height: 120.0">
        <a href=https://github.com/kaustav202>
            <img src=https://avatars.githubusercontent.com/u/89788120?v=4 width="80;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=kaustav202/>
            <br />
            <sub style="font-size:12px"><b>kaustav202</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 120.0; height: 120.0">
        <a href=https://github.com/segfal>
            <img src=https://avatars.githubusercontent.com/u/92688849?v=4 width="80;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=SegFal/>
            <br />
            <sub style="font-size:12px"><b>SegFal</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 120.0; height: 120.0">
        <a href=https://github.com/Rishav-12>
            <img src=https://avatars.githubusercontent.com/u/76068105?v=4 width="80;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Rishav Mitra/>
            <br />
            <sub style="font-size:12px"><b>Rishav Mitra</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 120.0; height: 120.0">
        <a href=https://github.com/Coder-Manan>
            <img src=https://avatars.githubusercontent.com/u/92792271?v=4 width="80;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Manan Garg/>
            <br />
            <sub style="font-size:12px"><b>Manan Garg</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 120.0; height: 120.0">
        <a href=https://github.com/gokullan>
            <img src=https://avatars.githubusercontent.com/u/84223229?v=4 width="80;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=gokullan/>
            <br />
            <sub style="font-size:12px"><b>gokullan</b></sub>
        </a>
    </td>
</tr>
</table>


<h2> Project Maintainers ⚡ </h2>
  <a href="https://github.com/kaustav202"></a>

---

## Happy Contributing! 🧡

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

Star Mark this repository and keep contributing as you learn!!
