
# Google Search CLI

This is a simple command-line tool that allows you to search Google from your terminal.

## Installation

To install, simply run `pip install search-terminal==0.0.1`.

## Usage

To use, simply run `go-search search <query>`. For example, to search for "cats", you would run `go-search search cats`.

The results will be printed to the terminal in JSON format.

At this point in development, the program takes only one argument as a query. If your search is multi-worded you might alternate to using `-` in between each word. For example, to search for "cats and mice", you would run `go-search search cats-and-mice`.


## Code Explanation

The code is relatively simple. The main function first checks to make sure that the user has provided a search query. If they have, it calls the `google_searcher()` function, which performs the search and returns the results. The results are then printed to the terminal in JSON format.

The `google_searcher()` function first makes a request to the Google search engine, using the user's query as the search term. If the request is successful, the function parses the HTML response and extracts the search results. The search results are then returned to the main function.

## Conclusion

This is a simple but useful tool that can be used to search Google from the command line. It is easy to use and install, and the code is well-commented and easy to understand.

If you are interested in helping develop this further you can contact me at "gmail: raymondbabalo5@gmail.com" or Instagram @ https://www.instagram.com/babalomajiyezi/ .
