# Finding the Ideal Drone YouTube Channel App

<img src="image/website.png" alt="Your Image" width="250"/>

## **Summary**
---
This application is designed to enhance the discovery process of drone-related YouTube channels, catering to specific interests or sponsorship requirements for Betafpv, a drone company. It addresses the challenges faced with traditional YouTube search methods, particularly in finding niche channels. By using TF-IDF analysis of the ten most recent videos from an input channel, the app generates a curated list of similar channels from our JSON database. This innovative approach ensures accurate and efficient channel recommendations, making it a tool for marketing departments like Betafpv seeking partnerships or for drone enthusiasts looking for content tailored to their preferences.

## **JSON Database**
---
The database is derived from another project and contains comprehensive statistics on drone YouTube channels, including:

- Channel Name
- Channel ID
- Subscriber Count
- Total Views
- Total Number of Videos
- Channel Category

Additionally, it provides detailed statistics for the five most recent videos of each channel:

- Video Title
- Description
- Published Date
- Tag Count
- View Count
- Like Count
- Dislike Count
- Comment Count

## **Building a Model for YouTube Channel Recommendation**
---
Channel similarity often resides within the video descriptions and titles. Our goal is to recommend channels based on the similarity of text descriptions using TF-IDF and cosine similarity. To achieve this, we retrieve the 10 most recent videos from the inputted YouTube channel and perform a similarity test against all channels in our database. This process ensures that users receive recommendations that closely match their preferences and interests, facilitating the discovery of new and relevant drone-related content.



----
### Learn about TF-IDF and cosine simliarity

TF-IDF is a statistical measure used to evaluate the importance of a word within a document relative to a collection of documents or a corpus. It is comprised of two components:

Term Frequency (TF): measures how frequently a term appears in a document.

Inverse Document Frequency (IDF): This measures the importance of the term across a set of documents.


Cosine similarity is a metric used to measure how similar two documents are irrespective of their size. For this project, each YouTube channel's video descriptions (after being processed through TF-IDF) are converted into vectors in a multidimensional space. Cosine similarity is then used to determine how similar an input channel's vector is to those of other channels in our database. Channels with the highest cosine similarity scores are considered the most similar and are recommended to the user.

