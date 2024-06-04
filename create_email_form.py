#FirstName, LastName, Company -> FirstName.LastName@company.com
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
company_name = input("Please enter your company name (no blank spaces): ")
print(f"{first_name}.{last_name}@{company_name}.com".lower())

email = f"{first_name}.{last_name}@{company_name}.com".lower()
print(email)
