# 10k-textmining

These are programs to count the number of occurences of key words from a large number of documents and store the information in a csv file.

1. Create new folder for tokenized text "tokenized_#"

2. Run "tokenize.py"
	- Change rootdir to location of data
	- Change save_path to ".../tokenized_#"

3. Create new csv file for results "report_#.csv"

4. Run "generatereport.py"
	- Change rootdir to ".../tokenized_#"
	- Change to open('report_#.csv', 'wb')
