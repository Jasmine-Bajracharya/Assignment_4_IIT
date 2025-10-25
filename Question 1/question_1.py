def main():
    # Note: Ensure that the current directory is the folder containing the code.

    while True:
        file_name = input('Please, enter the name of the file to be read: ')

        try:
            with open(file_name, 'r') as file:
                content = file.read().strip()
                age = int(content)
                print(f'Age: {age}')
            
            break
        except FileNotFoundError:
            print(f'File {file_name} not found.')
        except ValueError:
            print(f'File {file_name} contains an invalid age.')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    main()