# PR-Newswire.com_Scrapper
A python script to scrape press releases from prnewswire.com 

Go to https://www.prnewswire.com/ and search for any niche.

Change the search results to 100 per page.

You should get a url that looks like this ("https://www.prnewswire.com/news-releases/business-technology-latest-news/business-technology-latest-news-list/?page=1&pagesize=100")

substitute (page=1) for (page=" +str(page)+ "&pagesize=100)

This is so that you can itterate over multiple pages aka Pagination.

Also in the script set number_of_pages_to_scrape = "WHATEVER INTEGER YOU WANT"

