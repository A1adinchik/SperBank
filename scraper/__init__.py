from data import Quote, load_quotes
from download import Downloader
from parse import Parser


FILE_PATH = "random_quotes.html"
PARSED_FILE_PATH = "random_quotes_parsed.json"

def process():
    downloader = Downloader(url="http://bashorg.org/random", method="GET")
    downloader.save(FILE_PATH)
    parser = Parser(source=FILE_PATH)
    parser.parse()
    parser.save(PARSED_FILE_PATH)

    quotes = load_quotes(PARSED_FILE_PATH)
    quotes.sort(key=lambda q: q.rating or 0, reverse=True)
    
    return "\n====================\n".join(
        f"{quote.true_url} ({quote.rating}):\n{quote.quote}" 
        for quote in quotes[:3]
    )
