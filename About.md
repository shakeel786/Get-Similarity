# Approach

- step 1 :
First thing i have done is Cleaning of data
Data Cleaning :  - Coverting to lowercase, 
                 - Decoding utf-8 data
                 - removing html links using htmlparser
                 - removing stop words
                 - next Standardizing words (example making soooo haaaaapy to so hapy)
                 - removing duplicate words
                 - removing , data

After completion of Data cleaning of two resumes
- step 2 : 
  Grab of skills from resume files
              using keywords.txt file grabbed skills from resume files
              
-step 3 :
        Next we have to measure the similarity of two skils data
        count the no.of similar words, let us say n
        then total no.of words, let us say wn
        then fraction = n/wn
