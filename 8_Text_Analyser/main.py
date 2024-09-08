def open_file(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()

def analyse(text: str) -> dict[str, int]:
    result: dict[str, int] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_excl_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),   
        'total_words': len(text.split()),
    }

    return result

def main() -> None:
    text: str = open_file('note.txt')
    result: dict[str,int] = analyse(text)
    
    for key, value in result.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    main()