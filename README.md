# infoItem

## How to use?

Run 'python3 infoItem.py <file.txt>' on the command line. <file.txt> should be replaced by an actual .txt files where each line in the file contains a valid 27 character item ID. The program will identify and remove duplicate item ID's and then perform an HTTP get request for each item ID to the URL https://challenges.qluv.io/items/{itemID}. For each request's authorization, the program also must compute a base 64 string for each item ID to provide with the HTTP request. 

## Results

