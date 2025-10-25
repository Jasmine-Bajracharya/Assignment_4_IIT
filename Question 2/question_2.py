def main():
    while True:
        file_name = input('Please, enter the name of the file to be read: ')

        try:
            with open(file_name, 'r') as file:
                content = file.read().strip()
                age = int(content)
                print(f'Salary: ${age}')
                print('Thank you for using our program!!')
            
            break
        except FileNotFoundError:
            print(f'File {file_name} not found.')
            print('Try Again')
        except ValueError:
            print(f'File {file_name} contains an invalid salary.')
            print('Try Again')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            print('Try Again')

if __name__ == '__main__':
    main()