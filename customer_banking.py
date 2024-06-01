# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float( input("Please enter the savings account balance:   ") )                        #balance should be of float type because it can have dollars and cents
    savings_interest = float( input("Please enter the savings account interest rate:    ") )                #interest rate should also be float type because most of the time interest rate have decimal values as well
    savings_maturity = int( input("Please enter the number of months for the savings account:   ") )        #months can only be positive integers, so type should be int not float

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned in Savings account:     ${interest_earned_savings:.2f}")
    print(f"Updated Balance in Savings account:     ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float( input("Please enter the CD account balance:     "))                                #data types for cd variables are selected on the same criteria as for savings balance, interest and maturity
    cd_interest = float( input("Please enter the CD account interest rate:  "))
    cd_maturity = float( input("Please enter the number of months for the CD account:   "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest earned in CD Account:      ${interest_earned_cd:.2f}")
    print(f"Updated Balance in CD Account:      ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
