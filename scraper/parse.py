import json
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, source):
        self.FILE_PATH = source
        self.extracted_data = None
        
    def parse(self):
        with open(self.FILE_PATH) as f:
            html_code = f.read()
        self.extracted_data = self.extract_data(html_code)
        return self.extracted_data
        
    def extract_data(self, html_code):
        soup = BeautifulSoup(html_code, 'html.parser')
        data = {}
        return data
    
    def save(self, PARSED_FILE_PATH):
        if self.extracted_data is None:
            raise ValueError("Data has not been parsed yet. Call 'parse' method first.")
        with open(PARSED_FILE_PATH, 'w') as f:
            json.dump(self.extracted_data, f)


FILE_PATH = "weather.html"
PARSED_FILE_PATH = "weather.json"


parser = Parser(source=FILE_PATH)
parser.parse()