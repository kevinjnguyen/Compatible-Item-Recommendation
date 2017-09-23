# Overview
## Weeks 1 & 2 (September 18th - October 6th)
* Brainstorm ideas about what it means for something to be compatible. Can be gross assumptions. 
* Search for literary articles, research papers, and applicable databases to get more understanding on previous research on recommender systems. 
Understand the difference between previous research on recommender systems and how our research to create a new recommender system based on compatibility is different.
* Discuss with Dr. James Caverlee about presenting work publicly in Infolab in the following weeks after we have finished reading research papers on our topic. We will be giving a presentation about previous research papers that we read and what we have learned. This will allow other students in Infolab to understand our current research topic and how our research topic is different from previous research papers. 
* Discuss with Dr. James Caverlee about research compliance approval and whether or not we need research compliance approval with our current research project and future plans. If the answer is yes, we will need to attend a Research Compliance Informational and contact the office of Research Compliance & Biosafety and complete training/fill out forms to continue.
* Think more in depth about research question and describe even further what is means to be compatible based on literary articles.
* Start thesis statement for thesis, begin creating a thesis template, and download the thesis template that we want to use throughout the program.
Schedule project meetings with Dr. James Caverlee (faculty advisor) and Yin Zhang (graduate student advisor) weekly to discuss thesis template, installments, progress reports, thesis statement, and research progress.

# Schedule
## Tuesday, September 19th, 2017 Notes:
* Had weekly meeting with Dr. James Caverlee discussing research progress (getting datasets).
* Scheduled with Dr. James Caverlee for a research paper/project presentation on October 18th. 
* We will be presenting our top choice research article and how to improve the implementation as well as tying in our relation to these articles (introducing our project).
* We will include positive and negative aspects of the research article. 
* Discussed with Dr. James Caverlee and agreed that we DO need research compliance approval. We understand that we will have to attend a Research Compliance Informational and contact the office of Research Compliance & Biosafety and complete training/fill out forms to continue.

## Wednesday, September 20th, 2017 Notes:
* We are looking at the following link for applicable data about products featured on Amazon to get more understanding on previous research on recommender systems:
[http://jmcauley.ucsd.edu/data/amazon/](http://jmcauley.ucsd.edu/data/amazon/)
* Inside the data set provided by Julian McAuley, we will be analyzing the “small” subsets for experimentation data provided as well as the metadata datasets. 
* In this particular case, we began analyzing the electronics dataset as mentioned in our thesis.
The goal now would be to utilize the small subsets of data for information of the datasets and further apply our research to the complete sets of data.
* The electronic dataset provides useful information about reviews for electronics and the metadata provides information on products with their “also bought” and “also viewed” information. 
* Unfortunately we are not able to access the metadata information without requesting it from Julian McAuley directly. We are going to draft an email and ask for the data.
* Furthermore, the description of the product is not mentioned in the sample JSON provided but is mentioned in the description of the metadata. If the description of the item is not provided, our solution is to potentially use Amazon Product API and request that information manually.
* We hope to get the metadata and image features data by the end of next week, September 29th, 2017 so that we can analyze it.
* In the meantime, we will create scripts to assume the format of the JSON to read in the file into memory from mock data to prepare for when we receive the data and commit them to source control (Github) in Python.
* 2:59 PM, sent out email to Julian McAuley about the request access mentioned below. 
```
Julian McAuley (julian.mcauley@gmail.com)
Requesting for Metadata and image features data

Email (Access to Amazon review and product data):
Hello Professor McAuley, 

My name is Kevin J Nguyen, and I’m an undergraduate research student at Texas A&M University. I have found your research on the Amazon recommendation products fascinating. Currently with Victoria Wei (CC’ed on the email), we are researching under Dr. James Caverlee (also CC’ed on the email) on specific use cases in recommendation systems where compatibility might provide more relevant results for recommendation systems.

After taking a look at your research papers and the dataset you have provided online, we would like to request access to the per-category information of electronics on metadata and image features. We believe that access to this data will provide a tremendous asset to our undergraduate research. Please let me know if this is possible.

Thank you,

Kevin J Nguyen.

```

## Thursday, September 21st, 2017 Notes:
* Dr. Julian McAuley kindly provided us with the working links in minutes! 
* The working links are located at: [http://jmcauley.ucsd.edu/data/amazon/links.html](http://jmcauley.ucsd.edu/data/amazon/links.html).
* We are in the process of downloading the image features and electronics metadata into our laptops. Because the dataset is big, it will take ~1 day.
