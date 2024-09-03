def get_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def calculate_finance(monthly_income: float, tax_rate: float, currency: str, rent: float, groceries: float, gym: float, fuel: float, utilities: float) -> None:
    # Calculate monthly tax and net income
    monthly_tax = (tax_rate / 100) * monthly_income
    monthly_net_income = monthly_income - monthly_tax - rent - groceries - gym - fuel - utilities

    # Calculate yearly income, tax, and net income
    yearly_income = monthly_income * 12
    yearly_tax = monthly_tax * 12
    yearly_net_income = monthly_net_income * 12

    # Print the results
    print(f"Monthly Income: {currency}{monthly_income:,.2f}")
    print(f"Tax rate: {tax_rate}%")
    print(f"Monthly Tax: {currency}{monthly_tax:,.2f}")
    print(f"Monthly Net Income: {currency}{monthly_net_income:,.2f}")
    print("---------------------------------------------------")
    print(f"Yearly Income: {currency}{yearly_income:,.2f}")
    print(f"Yearly Tax: {currency}{yearly_tax:,.2f}")
    print(f"Yearly Net Income: {currency}{yearly_net_income:,.2f}")
    print("---------------------------------------------------")

def main() -> None:
    inputs = {
        "monthly_income": None,
        "tax_rate": None,
        "rent": None,
        "groceries": None,
        "gym": None,
        "fuel": None,
        "utilities": None
    }

    prompts = {
        "monthly_income": "Enter your monthly income: ",
        "tax_rate": "Enter your tax rate: ",
        "rent": "Enter your monthly rent: ",
        "groceries": "Enter your monthly groceries: ",
        "gym": "Enter your monthly GYM fee: ",
        "fuel": "Enter your monthly fuel expense: ",
        "utilities": "Enter your monthly utilities expense: "
    }

    for key in inputs:
        if inputs[key] is None:
            inputs[key] = get_input(prompts[key])

    calculate_finance(
        monthly_income=inputs["monthly_income"],
        tax_rate=inputs["tax_rate"],
        currency="₹",
        rent=inputs["rent"],
        groceries=inputs["groceries"],
        gym=inputs["gym"],
        fuel=inputs["fuel"],
        utilities=inputs["utilities"]
    )

if __name__ == "__main__":
    main()