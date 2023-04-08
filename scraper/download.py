import requests
from pathlib import Path


class Downloader:
    def __init__(self, url: str, method: str = "get", **params: dict):
        self.url = url
        self.params = params
        self.method = method.lower()

    def get_html(self) -> str:
        try:
            response = requests.request(self.method, self.url, **self.params)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return ""

    def save(self, file_path: str | Path) -> None:
        content = self.get_html()
        
        if not content:
            print("No content to save")
            return

        try:
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Error saving file: {e}")


URL = "http://bashorg.org/random"  # тут используйте адрес вашего сайта
# эти параметры также индивидуальны для страницы, которую вы скрапите
FILE_PATH = "quotes.html"  # используйте ваше название. Будет более понятно, если будете исполь-
# зовать расширение html, т.к. в этом файле будет код html-страницы

if __name__ == "__main__":
    downloader = Downloader(url=URL, method="GET")
    # этот метод возвращает строку с контентом, которую получил по запросу на URL
    print(downloader.get_html())
    # метод сохраняет полученную строку в файл, путь к которому подается в аргументе
    downloader.save(FILE_PATH)
