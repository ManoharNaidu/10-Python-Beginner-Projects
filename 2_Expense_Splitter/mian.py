def calculate_split(total_amount: float, no_of_ppl: int, currency: str, even_split: bool) -> None:
    if no_of_ppl < 1:
        raise ValueError("Number of people should be greater than 0")
    
    if not even_split:
        uneven_split = []
        for i in range(no_of_ppl):
            amount = float(input(f"Enter the percentage split for person {i + 1}: "))
            uneven_split.append(amount)
        
        total_percentage = sum(uneven_split)
        if total_percentage != 100:
            raise ValueError("Total percentage should be 100")

        for i in range(no_of_ppl):
            share = (uneven_split[i] / 100) * total_amount
            print(f"Person {i + 1} share: {currency}{share:,.2f}")
    else:
        shae_per_person = total_amount / no_of_ppl

        print(f"Total Amount: {currency}{total_amount:,.2f}")
        print(f"Number of people: {no_of_ppl}")
        print(f"Amount per person: {currency}{shae_per_person:,.2f}")


def main() -> None:
    try:
        total_amount = float(input("Enter the total amount: "))
        no_of_ppl = int(input("Enter the number of people: "))

        even_split = input("Do you want to split the amount evenly? (y/n): ")        

        calculate_split(total_amount, no_of_ppl, "₹", even_split=="y")
    
    except ValueError as e:
        print("Please enter a valid number", e)

if __name__ == "__main__":
    main()