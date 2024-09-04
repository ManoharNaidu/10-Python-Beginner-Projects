import re
from collections import Counter

def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_freq: Counter = Counter(words)

    return word_freq.most_common(n=5)

def read_file_content(file_path: str) -> str:
    try:
        file_path = file_path.strip('"')  # Strip any extra quotes
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return ""
    except OSError as e:
        print(f"Error opening file: {e}")
        return ""

def main() -> None:
    choice: str = input("Do you want to enter text directly or read from a file? (enter/file): ").strip().lower()

    if choice == "file":
        file_path: str = input("Enter the file path: ").strip()
        text: str = read_file_content(file_path)
        if not text:
            return
    else:
        text: str = input("Enter the text: ")

    freq: list[tuple[str, int]] = get_frequency(text)

    for word, count in freq:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()