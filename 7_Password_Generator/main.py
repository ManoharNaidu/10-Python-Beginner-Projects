import string
import secrets

class Password:
    def __init__(self, length: int = 16,use_uppercase: bool = True , use_numbers: bool = True, use_special_chars: bool = True) -> None:
        self.length = length
        self.useuse_uppercase =use_uppercase
        self.use_numbers = use_numbers
        self.use_special_chars = use_special_chars
        self.base_chars = string.ascii_lowercase

        if self.useuse_uppercase:
            self.base_chars += string.ascii_uppercase
        if self.use_numbers:
            self.base_chars += string.digits
        if self.use_special_chars:
            self.base_chars += string.punctuation
        
    def generate(self) -> str:
        password: list[str] = list(self.base_chars)
        return ''.join(secrets.choice(password) for _ in range(self.length))
    
    def check_strength(self) -> dict[int, str]:
        score = 0
        if self.length > 8:
            score += 1
        if  self.useuse_uppercase:
            score += 1
        if  self.use_numbers:
            score += 1
        if  self.use_special_chars:
            score += 1
        return {
            0: "Too Weak",
            1: "Weak",
            2: "Moderate",
            3: "Strong",
            4: "Very Strong"
        }[score]
        
        
    
    def __str__(self) -> str:
        return self.generate()

def main() -> None:
    password = Password()
    generated_password = str(password)
    print(f"Generated Password: {generated_password}")
    print(f"Password Strength: {password.check_strength()}")

if __name__ == "__main__":
    main()