# Import Packages Here:
from matplotlib import pyplot as plt
import wordcloud
import numpy as np

text ="""The goal of this book is to teach you to think like a computer scientist.This way of thinking combines some of the best features
of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal languages to denote ideas
(specifically computations). Like engineers, they design things, assembling components into systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, form hypotheses, and test predictions. 
The single most important skill for a computer scientist is problem solving.
Problem solving means the ability to formulate problems, think creatively about solutions, and express a solution clearly and accurately.
As it turns out, the process of learning to program is an excellent opportunity to practice problem-solving skills.
That’s why this chapter is called, “The way of the program.” 
On one level, you will be learning to program, a useful skill by itself. On another level, you will use programming as a means to an end.
As we go along, that end will become clearer.  The programming language you will learn is Python. Python is an example of a high-level 
language; other high-level languages you might have heard of are C, C++, Perl, and Java. 
There are also low-level languages, sometimes referred to as “machine languages” or “assembly languages.”
Loosely speaking, computers can only run programs written in low- level languages. So programs written in a high-level language have to be
processed before they can run.
This extra processing takes some time, which is a small disadvantage of high-level languages. 
The advantages are enormous.
First, it is much easier to program in a high-level language. Programs written in a high-level language take less time to write,
they are shorter and easier to read, and they are more likely to be correct. Second, high-level languages are portable,
meaning that they can run on different kinds of computers with few or no modifications.
Low-level programs can run on only one kind of computer and have to be rewritten to run on another. """

#To generate word_cloud image make sure you import WordCloud in your local system.

def calculate_frequencies(text):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~—+'“”'''
    uninteresting_words = ["the", "a", "to", "if", "is","in","it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we","us" ,"our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their","then", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few","for","more", "some", "such","on","no","not", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    word_dict = {}
    remove_punc = " "
    word_list = []
    #start by removing punctuation:
    for character in text:
        if character not in punctuations:
            remove_punc += character
        elif character == '-':
            remove_punc += character.replace('-'," ")
    punc_remvd_list = remove_punc.split()
    for word in punc_remvd_list:
        if word.lower() not in uninteresting_words:
            word_list.append(word.lower())
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    
    return word_dict
print(calculate_frequencies(text))
    #wordcloud
    #cloud = wordcloud.WordCloud()
    #cloud.generate_from_frequencies()
    #return cloud.to_array()

# Display your wordcloud image using inbuilt functions in python and save the resulting image.
# The path for the saving the plot image can be modified above to save it to the desired path.

myimage = calculate_frequencies(text)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
#plt.savefig(plot_path +'word_cloud'+'.png',bbox_inches='tight') 
##Uncomment and change the plt.savefig() as necessary.##
plt.show()