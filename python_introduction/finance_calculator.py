monthly_income= int(input("Enter your monthly income: ").strip())
monthly_expenses= int(input("Enter your total monthly expenses: ").strip())
monthly_savings= monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05

projected_savings = annual_savings + (monthly_savings * 12 * 0.05)
print(f"Your projected savings after one year, including 5% interest, is: {projected_savings}")
print(f"Your monthly savings are: {monthly_savings}")   