![Web App CI/CD](https://github.com/software-students-fall2024/5-final-finalfour/actions/workflows/web_app.yml/badge.svg?branch=main)

![Bar Recs CI/CD](https://github.com/software-students-fall2024/5-final-finalfour/actions/workflows/bar_recs.yml/badge.svg?branch=main)

[![Event Logger CI/CD](https://github.com/software-students-fall2024/5-final-finalfour/actions/workflows/event-logger.yml/badge.svg)](https://github.com/software-students-fall2024/5-final-finalfour/actions/workflows/event-logger.yml)


# HOME-BREWED: NYC BAR RECOMMENDER SYSTEM

***Home-Brewed*** is a versatile web application designed to enhance the way users explore, manage, and discover their favorite bars. This platform offers a personalized experience, catering to individual tastes and preferences, while simplifying the process of tracking and finding bars.
 
***Purpose:*** Crafted for individuals passionate about discovering new bars and managing personal experiences. Whether for casual outings, date nights, or special occasions, this app empowers users to make informed decisions while keeping track of their favorite spots.

## TABLE OF CONTENTS

1. [Description](#description)
2. [Setup Steps](#setup-steps)

## DESCRIPTION

***Home-Brewed*** is a web application designed to help users manage and explore their favorite bars based on personalized preferences. It provides a seamless user experience for adding, searching, sorting, editing, and receiving bar recommendations.

### Key Features

1. ***User Authentication:*** Secure login and logout features to ensure user sessions are protected.

2. ***Intuitive Navigation:*** A clean and organized navigation bar allows users to seamlessly switch between the key functionalities Home, Add, Edit/Delete, Search, Sort, and Reccomendations.
   
3. ***Add New Bars:*** Users can contribute by adding their favorite bars to the database with the categories name, type, occasion, area, if reservation is needed, cost, and if user visited.

4. ***Edit & Delete Existing Bars:*** Easily modify or remove existing entries to keep the bar database up-to-date and accurate.

5. ***Search for Bars:*** Quickly find bars that match specific criteria or keywords.
  
6. ***Sort Bars:*** Organize bars based on any category like occasion, area, cost, or if the user visited.
  
7. ***Personalized Recommendations:*** Displays a curated list of bars with details tailored to user preferences based on the saved bars.

## SETUP STEPS

**1. Clone & Setup Repository:**

```
cd Desktop
git clone https://github.com/reeseburns/NYC-Bars-App.git
cd NYC-Bars-App/web_app
python3 -m venv .venv
source .venv/bin/activate
```

**2. Install Dependencies:**
```
pip install opencv-python-headless
pip install pytest pytest-cov
pip install python-dotenv
pip install pymongo
pip install -r requirements.txt
```

**3. Install Docker-Compose:**

```
brew install docker-compose
docker-compose down --volumes --remove-orphans
docker-compose up --build
```

**Get Drinking!** [Home-Brewed](http://104.236.30.209:5000/)
