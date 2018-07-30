# code-challenge

# Usage
To run the first challenge and its unittest you need to type `python challeng1.py` and 
`python challenge1Test.py` in your terminal window respectively.

To run the second challenge and its unittest you need to type `python challenge2.py` and
`python challenge2Test.py` in your termianl window respectively.

One thing I like about my implementation in challenge one is that I break the loop as soon as I find a digit in the number which is not even. In the short run this may not seem to be significant but if millions of numbers are processed, this could save a good amount of work.

About the second challenge, there are different ways of implementing that. This includes applying regex or using external libraries such as dateutil to parse the date column of the csv file. But to me using regex sounds overkill here when I can just use built-in string methods such as split. If it was a production process I would use the external dateutil library but since this is a test for me, I wanted to show that I can solve the problem without using the external library.

For the second challenge, I broke down the problem into two parts. The first part focuses on parsing an individual row and extracting the parameters to sort by. The second part does the reading csv file and the actual sorting.