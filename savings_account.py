"""Import the Account class from the Account.py file."""
import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    my_savings_account = Account(balance,0)

    # Calculate interest earned
    my_savings_interest = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    my_savings_balance = balance + my_savings_interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    my_savings_account.set_balance( my_savings_balance )

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    my_savings_account.set_interest( my_savings_interest )

    # Return the updated balance and interest earned.
    return  my_savings_balance, my_savings_interest
