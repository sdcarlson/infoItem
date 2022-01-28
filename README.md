# infoItem

## How to use?

Run 'python3 infoItem.py <file.txt>' on the command line. <file.txt> should be replaced by an actual .txt files where each line in the file contains a valid 27 character item ID. An example of a valid input file is items.txt which you can find in this repo. The program will identify and remove duplicate item ID's and then perform an HTTP get request for each item ID to the URL https://challenges.qluv.io/items/{itemID}. For each request's authorization, the program also must compute a base 64 string for each item ID to provide with the HTTP request. 

## Results

The output from running this program will be many pairs of strings with the first one being the item ID and the second one representing the data returned by a GET request to that item's url. There will be a line in standard output for every unique item ID in the specified input file. The ordering of item IDs in the program's output will not match that of the original file due to the non-deterministic nature of multithreading. 

## Timing

I used the 'time' module to measure the efficiency of my program. The timer is started once all the input item Ids are parsed and we are about to start sending out HTTP requests. After all the HTTP requests have been sent out, the timer stops and the average time per item ID is printed to standard output.
