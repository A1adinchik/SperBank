import json
from typing import List, Optional
import webbrowser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Quote:
    quote: Optional[str] = None
    url: Optional[str] = None
    rating: Optional[int] = None

    base_url: str = "http://bashorg.org"

    def is_valid(self) -> bool:
        return all([self.quote, self.url, self.rating])

    @property
    def true_url(self) -> Optional[str]:
        if self.url is None:
            return None
        return f"{self.base_url}{self.url}"

    def open(self) -> None:
        if self.true_url is not None:
            webbrowser.open(self.true_url)


def load_quotes(filename: str | Path) -> List[Quote]:
    with open(filename, "r") as f:
        try:
            quotes = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Failed to load {filename}: {e}")
            return []

    result = []
    for q in quotes:
        try:
            result.append(Quote(**q))
        except TypeError as e:
            print(f"Failed to load quote from {filename}: {e}")
    return result


if __name__ == "__main__":
    quotes = load_quotes("quotes.json")
    quotes.sort(key=lambda q: q.rating, reverse=True) # type: ignore
    print(f"Best quote: {quotes[0]}")
    if input("Open in browser? (y/n): ") == "y":
        quotes[0].open()
    