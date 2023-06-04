# Password Generator 

This Python-based password generator is a secure, efficient, and user-friendly tool that's perfect for creating unique, encrypted passwords. It uses a powerful combination of hashing, a key derivation function, and base64 encoding to generate highly secure passwords from a master password and a unique metadata input (like a username or a site name).

## Why This Password Generator?

When it comes to managing our digital lives, security is paramount. A strong, unique password is your first line of defense against unauthorized access and potential data breaches. However, remembering a myriad of complex passwords can be a daunting task. This is where this password generator comes into play.

In this application, you don't need to remember every password for every account; instead, you only need a master password and the unique metadata associated with each account (such as the username or the website's name). This keeps the usage simple and anonymous while ensuring that each password is unique and secure. Moreover, each generated password can be saved securely and retrieved later, adding a handy password management feature to this tool.

## Features

- **Secure Password Generation**: The tool uses the PBKDF2HMAC key derivation function with SHA-256 hashing and 100,000 iterations to generate a secure key from the master password and the metadata. This key is then base64-encoded to create a safe, usable password.
- **Easy Copy and Save**: You can easily copy the generated password to the clipboard or save it for later use with a simple click. All saved passwords are encrypted and stored securely.
- **Simplicity and Anonymity**: Unlike many other password managers or generators, this tool doesn't require any user accounts or personal information. All you need is your master password and metadata to start generating secure passwords.
- **Built-in Confirmation Mechanism**: Before saving any password, the application will always ask for your confirmation, ensuring that you have full control over which passwords get stored.

## Setup and Compilation

You need to have Python 3 installed on your machine to run this tool.

1. Clone this repository to your local machine.

2. Navigate to the directory containing the Python script (`password_generator.py`).

3. Before running the program, ensure that you have the necessary packages installed. If not, you can install them using pip:
   
   ```
   pip install tkinter
   pip install cryptography
   ```

4. Run the script with Python:

   ```
   python password_generator.py
   ```

To compile this into a standalone executable, you can use `PyInstaller`:

1. Install PyInstaller:

   ```
   pip install pyinstaller
   ```

2. Navigate to the directory containing your Python script (`password_generator.py`), then type:

   ```
   pyinstaller --onefile password_generator.py
   ```

3. PyInstaller will create a `dist/` folder in the same directory as your script. Inside this `dist/` folder, you'll find your standalone executable.

## Contribution

Feel free to fork this project, open issues, or submit pull requests. Any contributions are welcomed and appreciated.

## License

This project is licensed under the terms of the MIT license.
