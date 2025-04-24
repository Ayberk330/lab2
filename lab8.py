import datetime

class ArchiveItem:
    
    def __init__(self, uid: str, title: str, year: int):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self) -> str:
        return f"{self.uid}: '{self.title}' ({self.year})"

    def __eq__(self, other) -> bool:
        return isinstance(other, ArchiveItem) and self.uid == other.uid

    def is_recent(self, n: int) -> bool:
        reference_year = 2025
        return self.year >= reference_year - n


class Book(ArchiveItem):
    def __init__(self, uid: str, title: str, year: int, author: str, pages: int):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{super().__str__()} by {self.author}, {self.pages} pages"


class Article(ArchiveItem):
    def __init__(self, uid: str, title: str, year: int, journal: str, doi: str):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self) -> str:
        return f"{super().__str__()} in {self.journal}, DOI: {self.doi}"


class Podcast(ArchiveItem):
    def __init__(self, uid: str, title: str, year: int, host: str, duration: int):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self) -> str:
        return f"{super().__str__()} hosted by {self.host}, duration {self.duration} min"


def save_to_file(items: list, filename: str):

    with open(filename, 'w', encoding='utf-8') as f:
        for item in items:
            if isinstance(item, Book):
                line = f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}"
            elif isinstance(item, Article):
                line = f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}"
            elif isinstance(item, Podcast):
                line = f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}"
            else:
                continue
            f.write(line + '\n')


def load_from_file(filename: str) -> list:

    items = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            typ = parts[0]
            if typ == 'Book' and len(parts) == 6:
                _, uid, title, year, author, pages = parts
                item = Book(uid, title, int(year), author, int(pages))
            elif typ == 'Article' and len(parts) == 6:
                _, uid, title, year, journal, doi = parts
                item = Article(uid, title, int(year), journal, doi)
            elif typ == 'Podcast' and len(parts) == 6:
                _, uid, title, year, host, duration = parts
                item = Podcast(uid, title, int(year), host, int(duration))
            else:
                continue
            items.append(item)
    return items


if __name__ == '__main__':
    items = [
        Book('B001', 'Deep Learning', 2018, 'Ian Goodfellow', 775),
        Book('B002', 'Clean Code', 2008, 'Robert C. Martin', 464),
        Article('A001', 'Attention Is All You Need', 2017, 'NeurIPS', '10.5555/3295222.3295349'),
        Article('A002', 'A Survey on Transfer Learning', 2010, 'IEEE TKDE', '10.1109/TKDE.2009.191'),
        Podcast('P001', 'Tech Trends', 2024, 'Jane Doe', 52),
        Podcast('P002', 'AI Insights', 2025, 'John Smith', 48),
    ]

    filename = 'archive.txt'
    save_to_file(items, filename)
    print(f"Saved {len(items)} items to {filename}.")

    loaded_items = load_from_file(filename)
    print(f"Loaded {len(loaded_items)} items from {filename}:")

    for obj in loaded_items:
        print(obj)
