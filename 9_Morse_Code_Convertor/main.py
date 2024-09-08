morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def convert_to_morse_code(text: str) -> str:
    return ' '.join([morse_code_dict.get(char.upper(), '') for char in text])

def convert_from_morse_code(morse_code: str) -> str:
    reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}
    return ''.join([reverse_morse_code_dict.get(code, '') for code in morse_code.split(' ')])

def main() -> None:
    while True:
        user_input: str = input('Choose any one: \n1 to convert text to Morse Code \n2 to convert Morse Code to text\n\n ')

        if user_input == '1':
            text: str = input('Enter text to convert to Morse Code: ')
            print(f'Morse Code: {convert_to_morse_code(text)}')
            break
        elif user_input == '2':
            morse_code: str = input('Enter Morse Code to convert to text: ')
            print(f'Text: {convert_from_morse_code(morse_code)}')
            break
        else:
            print('Invalid input. Please enter 1 or 2.')

if __name__ == '__main__':
    main()