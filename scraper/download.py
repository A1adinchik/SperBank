import requests

class Downloader:
    def __init__(self, url, params=None, method='get'):
        self.url = url
        self.params = params
        self.method = method.lower()
    
    def download(self):
        if self.method == 'get':
            response = requests.get(self.url, params=self.params)
        elif self.method == 'post':
            response = requests.post(self.url, data=self.params)
        else:
            raise ValueError('Unsupported method: %s' % self.method)
        
        if response.status_code != 200:
            raise ValueError('Failed to download page: %s' % response.text)
        
        return response.text
    
    def save(self, file_path):
        content = self.get_html()
        with open(file_path, 'w') as f:
            f.write(content)
    
    def get_html(self):
        return self.download()

URL = "http://www.hmn.ru/index.php"      # тут используйте адрес вашего сайта
PARAMS = {                               # эти параметры также индивидуальны для страницы, которую вы скрапите
    "index": 8,
    "value": 22113,
    "tz": 3,
    "start": "2022-11-20",
    "fin": "2022-11-28",
    "x": 10,
    "y": 5,
}
FILE_PATH = "weather.html"               # используйте ваше название. Будет более понятно, если будете исполь-
                                         # зовать расширение html, т.к. в этом файле будет код html-страницы

downloader = Downloader(url=URL, params=PARAMS, method="GET")
print(downloader.get_html())       # этот метод возвращает строку с контентом, которую получил по запросу на URL
downloader.save(FILE_PATH)  # метод сохраняет полученную строку в файл, путь к которому подается в аргументе