# Textmining for 10-K reports

These are programs to count the number of occurences of key words from a large number of documents and store the information in a csv file.

Steps to do it yourself:

1. Create new folder for tokenized text "tokenized_#"

2. Run "tokenize.py"
	- Change rootdir to location of data
	- Change save_path to ".../tokenized_#"

3. Create new csv file for results "report_#.csv"

4. Run "generatereport.py"
	- Change rootdir to ".../tokenized_#"
	- Change to open('report_#.csv', 'wb')

*Note you will have to change the directories to your own for each variable.


## Improving the code

The algorithms and important functions are included in the code, but there are definitely areas for improvement. The main issue is a lack of generalizing the functions, making the code less flexible. Moreover, it wouldn't be too difficult to simplify the code for use by beginners. 

Other improvements for future versions:
 - Better documentation of times and progress
