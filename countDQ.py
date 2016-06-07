#import necessary libraries
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
import string
import os
import timeit
import csv
from os.path import basename
import tempfile



#initialize the results array 
results = []
#list of words to check
undWords = ['digital', 'electronic', 'analytics', 'online', 'internet', 'cloud', 'ecommerce']
upWords = ['IT', 'RFID']
phrases = ['bigdata', 'informationtechnology']



#start a timer
start = timeit.default_timer()

#store file paths to a list
print 'storing the original files to a list...'
rootdir = '/media/xvdb1'

list_10k = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        list_10k.append(os.path.join(subdir, file))
print 'finished storing the original files...'



#analyze each file
#intialize file counter
count = 1
for k in list_10k:

   #save original path name
   kk = k

   print 'removing unnecessary elements from the file (#' + str(count) + ')...'
   raw = open(k).read()

   #remove html elements from the raw text
   noH = re.sub('<[^>]*>', '', raw)
   noH = re.sub('&.*?;', '', noH)
   
   #combine DQ phrases to one word
   noH = re.sub('big data','bigdata', noH)
   noH = re.sub('information technology','informationtechnology', noH)
   noH = re.sub('e-commerce','ecommerce', noH)
   
   #remove all remaining punctuation
   exclude = set(string.punctuation)
   noH = ''.join(ch for ch in noH if ch not in exclude)

   #remove all numbers
   noH = ''.join(i for i in noH if not i.isdigit())

   #add noH to a temporary file
   print 'creating a temporary file...'
   temp = tempfile.TemporaryFile()
   try:
           temp.write(noH)
           temp.seek(0)
           pt = temp.read()
           #tokenize the temporary file and set it to a new variable
           tokens = word_tokenize(pt)
   finally:
           temp.close()

   #store all the lowercase values of the tokens
   low_tokens = [x.lower() for x in tokens]
  
   #create lists of matches
   dq_undWords = [w for w in low_tokens if w in undWords]
   dq_upWords = [k for k in tokens if k in upWords]
   dq_phrases = [l for l in low_tokens if l in phrases]               
  
   #calculate totals of DQ words and entire document
   totDQ = len(dq_undWords) + len(dq_upWords) + len(dq_phrases)
   #add the number of phrases because they are 2 words long
   tot = len(tokens) + len(dq_phrases)
   
   #for undWords
   totDi = dq_undWords.count('digital')
   totEl = dq_undWords.count('electronic')
   totAn = dq_undWords.count('analytics')
   totOn = dq_undWords.count('online')
   totIn = dq_undWords.count('internet')
   totCl = dq_undWords.count('cloud')
   totEc = dq_undWords.count('ecommerce')
   
   #for upWords
   totIT = dq_upWords.count('IT')
   totRF = dq_upWords.count('RFID')
   
   #for phrases
   totBi = dq_phrases.count('bigdata')
   totInfo = dq_phrases.count('informationtechnology')

   #remove path and extension from file name, only include id number in the csv report
   r_k = os.path.splitext(kk)[0]
   r_k = basename(r_k)

   #initialize coR list with ['name', '', '', '', '', '', '', '', '', '', '', '', 'total number of DQ words', 'total number of words in the report' ]
   coR = []
   coR.append(r_k)
   coR.append(str(totDi))
   coR.append(str(totEl))
   coR.append(str(totAn))
   coR.append(str(totOn))
   coR.append(str(totIn))
   coR.append(str(totCl))
   coR.append(str(totEc))
   coR.append(str(totIT))
   coR.append(str(totRF))
   coR.append(str(totBi))
   coR.append(str(totInfo))
   coR.append(str(totDQ))
   coR.append(str(tot))

   #add coR to results list
   print 'Results for ' + r_k + ' added'
   results.append(coR)
 
   #increment counter
   count = count + 1



#write results to the csv file
print '\n'
print 'Writing the data to a csv file...'
length = len(results[0])
with open('report_test.csv', 'wb') as f:
   file_writer = csv.writer(f)
   for y in range(length):
      file_writer.writerow([x[y] for x in results])
print 'Finished.'
print '\n'


#print runtime information
print 'Total number of documents analyzed: ' + str(count - 1)
stop = timeit.default_timer()
time = stop - start
print 'Total runtime: ' + str(time) + ' seconds'
print 'Runtime per file: ' + str(time/(count-1)) + ' seconds'
print '\n'

