from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
import string
import os
import timeit
import csv

start = timeit.default_timer()

#store plain text file paths to a list
print 'storing plain text files to a list...'
rootdir = '/home/jsyz/Desktop/tokenized'

pt_list_10k = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        pt_list_10k.append(os.path.join(subdir, file))
print 'finished storing plain text files...'

#list of words to check
undWords = ['digital', 'electronic', 'analytics', 'online', 'internet', 'cloud', 'ecommerce']
upWords = ['IT', 'RFID']
phrases = ['bigdata', 'informationtechnology']

#initialize results array
results = []

#determine results for each document
c = 1
for kk in pt_list_10k:
   print 'analyzing file ' + str(c) + '...'
   pt = open(kk).read()
   
   #tokenize the text
   tokens = word_tokenize(pt)
   
   #store all the lowercase values of the tokens
   low_tokens = [x.lower() for x in tokens]
   
   #create lists of matches
   dq_undWords = [w for w in low_tokens if w in undWords]
   dq_upWords = [k for k in tokens if k in upWords]
   dq_phrases = [l for l in low_tokens if l in phrases]
   
   #calculate totals of DQ words and entire document
   totDQ = len(dq_undWords) + len(dq_upWords) + len(dq_phrases)
   tot = len(tokens) + len(dq_phrases)
   
   #calculate totals of each word
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
   
   #initialize coR list with ['name', '', '', '', '', '', '', '', '', '', '', '', 'total number of DQ words', 
   #'total number of words in the report' ]
   coR = []
   coR.append(kk)
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
   print 'Results for ' + kk + ' added'
   results.append(coR)
   
   #increment counter
   c = c + 1


print '\n'
print 'Writing data to a report'
#write data to the csv file
length = len(results[0])
with open('report.csv', 'wb') as f:
   file_writer = csv.writer(f)
   for y in range(length):
        file_writer.writerow([x[y] for x in results])
print 'Finished.'
print '\n'

print 'Total number of documents analyzed: ' + str(c - 1)

stop = timeit.default_timer()
time = stop - start

print 'Total runtime: ' + str(time) + ' seconds'




























