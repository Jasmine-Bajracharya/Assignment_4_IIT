import tkinter as tk
from tkinter import messagebox
import os

def read_file():
    file_name = e1.get().strip()  # Get the filename from the entry box
    base_dir = os.getcwd()        # Current working directory
    full_path = os.path.join(base_dir, file_name)

    try:
        with open(full_path, 'r') as file:
            content = file.read().strip()
            age = int(content)
            messagebox.showinfo("Success", f"Age: {age}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_name}' not found in:\n{base_dir}")
    except ValueError:
        messagebox.showerror("Error", f"File '{file_name}' contains an invalid age.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

def main():
    global e1  # to make e1 accessible inside read_file()
    root = tk.Tk()
    root.title("Solution of Question 8")
    root.geometry("500x250")
    root.configure(bg="#f0f8ff") #setting the background color to light blue


    label = tk.Label(root, text="Enter the name of the file to be read:", bg="#f0f8ff" , fg= "Blue")
    label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    e1 = tk.Entry(root, width=50, justify="center") #using the entry box to take input form the user for the file to be read
    e1.grid(row=2, column=0, padx=10, pady=5)

    read_btn = tk.Button(root, text="Read File", command=read_file, bg="white", fg="black")
    read_btn.grid(row=3, column=0, pady=15)

    root.mainloop()

if __name__ == '__main__':
    main()

