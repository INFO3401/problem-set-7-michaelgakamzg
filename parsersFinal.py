################################################################################
# Worked with Brandon and Aaron

# PART #1
################################################################################
import csv
import string
from collections import Counter
from os import listdir
import os
import glob
import json
import sqlite3

def countWordsUnstructured(filename):
    
    wordCounts = {}
    datafile = open(filename).read()
    data = datafile.split()
    
    for word in data:
        for mark in string.punctuation:
            word = word.replace(mark,"")
        if word in wordCounts:
            wordCounts[word] = wordCounts[word] + 1
        else: wordCounts[word] = 1
    return wordCounts


    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts

bush1989 = countWordsUnstructured("./state-of-the-union-corpus-1989-2017/Bush_1989.txt")
print (bush1989)

# PART 2
################################################################################

def generateSimpleCSV(targetfile, wordCounts):
# This function should transform a dictionary containing word counts to a
# CSV file. The first row of the CSV should be a header noting:
# Word, Count
# Inputs: A word count list and a name for the target file
# Outputs: A new CSV file named targetfile containing the wordcount data

    with open('1989.csv', 'w') as my_file:
        
        writer = csv.writer(my_file)
        writer.writerow(['Word','Count'])
        for key, value in bush1989.items():
            writer.writerow([key,value])

generateSimpleCSV('1989.csv' , bush1989)


#Pring the Headers

#Iterate through the word counts
    #Add to our CSV file
#Close file

#Return pointer to file


# Test your part 2 code below

#Part 3
################################################################################

def countWordsMany(directory):
	dictionary = {}
	files = glob.glob(os.path.join(directory, '*.txt'))
	for fle in files:
		dictionary[fle] = countWordsUnstructured(fle)
	return (dictionary)

directoryCount = countWordsMany("./state-of-the-union-corpus-1989-2017")


#Part 4

def generateDirectoryCSV(wordCounts, targetfile):
    with open ('new.csv', 'w') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(['Filename','Word', 'Count'])
        for k, v in directoryCount.items():
            for key, value in v.items():
                writer.writerow([k,key, value])

generateDirectoryCSV(directoryCount, 'new.csv')


#Part 5

def generateJSONFile(wordCounts, targetfile):
    with open('result.json', 'w') as fp:
        json.dump(directoryCount, fp)

generateJSONFile(directoryCount, 'result.json')


