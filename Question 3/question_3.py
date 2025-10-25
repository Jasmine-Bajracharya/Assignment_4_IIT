def main():
    while True:
        try:
            value = int(input("Enter an integer between 1 to 10: "))

            # Used assert to prevent the use of if..else statement as using ValueError requires using if..else statement.
        
            assert value != 0, "Opps, you entered zero."
            assert 1 <= value <= 10, "You did not enter a number between 1 and 10!!!"

            print(f"The Reciprocal of your number is {1 / value}")
            break
        except AssertionError as e:
            print(e)
            print('Please, try again.\n')
        except ValueError:
            print('You did not enter an integer!!!')
            print('Please, try again.\n')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            print('Please, try again.\n')

if __name__ == '__main__':
    main()