from __future__ import division
import nltk, re, pprint
import string
import os


#store file paths to a list
print 'storing files to a list...'
rootdir = '/home/jsyz/Desktop/data - Copy'

list_10k = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        list_10k.append(os.path.join(subdir, file))
print 'finished storing files...'


#create new files for all of the reports
count = 1
for k in list_10k:
   print 'processing file ' + str(count) + '...'
   raw = open(k).read()
   
   #remove html elements from the raw text
   noH = re.sub('<[^>]*>', '', raw)
   noH = re.sub('&.*?;', '', noH)
   
   #combine DQ phrases to one word
   noH = re.sub('big data','bigdata', noH)
   noH = re.sub('information technology','informationtechnology', noH)
   noH = re.sub('e-commerce','ecommerce', noH)
   
   #remove all remaining punctuation
   #TO-DO: find way to keep track of where in a sentance the word is				
   exclude = set(string.punctuation)
   noH = ''.join(ch for ch in noH if ch not in exclude)
   
   #remove all numbers
   noH = ''.join(i for i in noH if not i.isdigit())
   
   #append plain text to a file, saved in the 'tokenized' folder
   print 'creating file for ' + str(count) + ' and saving it to a folder...'
   save_path = '/home/jsyz/Desktop/tokenized/'
   head, tail = os.path.split(k)
   name_of_file = tail
   completeName = os.path.join(save_path, name_of_file)         
   file1 = open(completeName, "w")
   file1.write(noH)
   file1.close()
   print 'file for ' + str(count) + ' completed'
   
   #increment counter
   count = count + 1








