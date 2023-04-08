import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.element import Tag


def extract_quote_data(element: Tag):
    result = {
        "quote": None,
        "url": None,
        "rating": None,
    }

    try:
        for div in element.find_all('div'):
            class_ = div.get("class")
            if class_ and class_[0] == "quote":
                result["quote"] = div.get_text("\n").strip()
            elif class_ and class_[0] == "vote":
                result["url"] = div.find('a')['href']
    except Exception as e:
        print(f"Error occurred while extracting quote data: {e}")

    try:
        rating_element = element.find("span", id=re.compile(r"result-(\d+)"))
        result["rating"] = int(rating_element.get_text()) if rating_element else None # type: ignore
    except Exception as e:
        print(f"Error occurred while extracting rating data: {e}")
    
    return result


class Parser:
    def __init__(self, source):
        self.FILE_PATH = source
        self.extracted_data = None

    def parse(self):
        try:
            with open(self.FILE_PATH) as f:
                html_code = f.read()
            self.extracted_data = self.extract_data(html_code)
            return self.extracted_data
        except Exception as e:
            print(f"Error occurred while parsing HTML code: {e}")

    def extract_data(self, html_code):
        try:
            soup = BeautifulSoup(html_code, "html.parser")
            elements = soup.find_all("div", {"class": "q"})
            data = []
            for quote in elements:
                data.append(extract_quote_data(quote))
            return data
        except Exception as e:
            print(f"Error occurred while extracting data: {e}")

    def save(self, PARSED_FILE_PATH):
        if self.extracted_data is None:
            raise ValueError("Data has not been parsed yet. Call 'parse' method first.")
        try:
            with open(PARSED_FILE_PATH, "w") as f:
                json.dump(self.extracted_data, f, indent=2)
        except Exception as e:
            print(f"Error occurred while saving parsed data: {e}")


FILE_PATH = "quotes.html"
PARSED_FILE_PATH = "quotes.json"

if __name__ == "__main__":
    parser = Parser(source=FILE_PATH)
    parser.parse()
    parser.save(PARSED_FILE_PATH)
