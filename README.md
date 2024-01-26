# Finding the ideal Drone Youtube Channel APP



## **Summary:**
----

####    This application is engineered to streamline the discovery of drone-related YouTube channels tailored to specific interests or sponsorship criteria. Recognizing the limitations of conventional search methods on YouTube, especially when pinpointing niche channels, this app introduces a targeted approach. It leverages a sophisticated tf-idf analysis of the ten most recent videos from a given channel to generate a curated list of similar channels. This method ensures precision and efficiency in identifying potential channels for partnerships or personal enjoyment, thereby optimizing your search strategy on YouTube.

### **Data Scraping and Cleaning:**
----

####     From my other project, I have built a Json databse of all the drone youtube Channel 

### **Building Model for Recipe Recommendation:**

----

####     Constructing an effective recommendation model involved utilizing TF-IDF (Term Frequency-Inverse Document Frequency) to evaluate the significance of each ingredient. TF-IDF works by assigning weights to words based on their frequency in a specific document relative to their frequency across all documents. In the context of our app, each recipe is treated as a document, and the ingredients as the words.

####     To optimize the model, I eliminated common ingredients such as salt, pepper, water, etc. Though essential in cooking, could potentially skew the recommendation results. The step was measuring the similarity between the user-provided ingredients and the database of ingredients using cosine similarity. It refines the recommendations by filtering out the top similar recipes, ensuring that users receive the most similar recipes. For example, let's consider a scenario where a user inputs "kimchi" and "tofu" as ingredients. The recommendation model, after TF-IDF processing and cosine similarity calculation, filters through the database to present recipes prioritizing recipes that have kimchi as this is a more significant ingreident.

####     While attempting to enhance the recommendation model, I attempted to use Word2Vec, a powerful word embedding technique, However, through experiment, it became evident that the performance of the model did not improve; in fact, it appeared to worsen. This observed decline is due to inherent challenges posed by certain Korean ingredients, whose meanings may not be effectively captured by the Word2Vec embedding. 

