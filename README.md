# Python-text-scraper
This script scraps data (Text) from a given link and calculate some parameters from the it. This script works for pages of a given website at a time.

at the moment it is using "Input - Copy.csv" for the urls and the website right now is TimesOfIndia whose five articles are being scraped.

## Additional Packages Required:
- Pandas
- requests_html

## Instructions to use and what it does:
"Cell.py" is our main python file. "semipermeable_membrane.py" holds scraping (and some cleaning) part of the script:

-Say if you want to scrape another website then on that website find the class inder which the required text content is and paste the class name in this line _tmptxt = (htmlctx.xpath('.//div[@class="main-content single-article-content"]//text()'))

and "the_system.py" contains functions that calculates these variables:
- POSITIVE SCORE
- NEGATIVE SCORE
- POLARITY SCORE
- SUBJECTIVITY SCORE
- AVG SENTENCE LENGTH
- PERCENTAGE OF COMPLEX WORDS
- FOG INDEX
- COMPLEX WORD COUNT
- SYLLABLE PER WORD
- AVG WORD LENGTH
- WORD COUNT
- PERSONAL PRONOUNS

some of these variables are calculated with the help of ["MasterDictionary.txt"](https://sraf.nd.edu/textual-analysis/resources/) and cleaning function remove stop words using [StopWords_GenericLong.txt](https://sraf.nd.edu/textual-analysis/resources/).
