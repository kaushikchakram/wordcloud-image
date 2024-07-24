# This repository is based on an assignment in Coursera course called "Crash Course on Python by Google."

<This was the final project assignment for that course and this was my submission for it. 
I have modified the original submission document with comments where necessary as a guide for the user.>   

### The repository contains three main files: 
+ `word_cloud.ipynb` which is the main jupyter notebook file that the user can access and should work provided the local paths are modified as needed.
+ `word_cloud.png` this is the result of the code that is generated from `word_cloud.ipynb`
+ `word_cloud_image.py` does essentially the same thing as `word_cloud.ipynb`, but it is .py version for the user convenience. 
+ **Note: `word_cloud_image.py` assumes that `WordCloud` module, `numpy`, `matplotlib` are intalled in the local computer where it is run.**

### The Goal of `word_cloud.ipynb` notebook is to generate a wordcloud image based on some input text.

+ The process is as follows:
   + Upload some input text
&rarr; disregard puncutation and uninteresting words like "the","as","and" etc. &rarr; calculate frequencies of the interesting words (i.e. number of occurences of these words) in the input text &rarr; then use the frequencies to generate the wordcloud image.

The word cloud image essentially weights highly frequent words with a bolder and a larger fontsize relative to less frequent words.
