# Caesar Cipher Program 

## Overview
`task1.py` is a command-line tool for encrypting and decrypting messages using the Caesar Cipher technique. It features an interactive menu allowing users to select options for encryption, decryption, and exiting the program. This tool is designed as an introduction to basic cryptography principles in Python.

## Features
- **Encrypt Messages**: Shift characters in a message to generate encrypted text.
- **Decrypt Messages**: Reverse the shift to retrieve the original message.
- **Custom Shift Value**: Users specify the shift value to control the cipher's rotation.

## Requirements
The script requires **Python 3** and the `colorama` library for colorized command-line output.

### Installation
1. Install Python 3 if it’s not already installed. You can download it [here](https://www.python.org/downloads/).
2. Install dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the script, use the following command:

```bash
python3 task1.py
```

The script will display a banner and offer options for encryption, decryption, and quitting.

## Example Output
An example interaction with the script:

```plaintext
========================================
      Welcome to Caesar Cipher Program      
========================================
Author: G4UR4V007   Version: 1.0
========================================

Caesar Cipher Options
1. Encrypt a message
2. Decrypt a message
3. Quit
Choose an option (1/2/3): 1
Enter a message to encrypt: Hello World
Enter a shift value (integer): 3
Encrypted text: Khoor Zruog

Caesar Cipher Options
1. Encrypt a message
2. Decrypt a message
3. Quit
Choose an option (1/2/3): 2
Enter a message to decrypt: Khoor Zruog
Enter a shift value (integer): 3
Decrypted text: Hello World
```

## License
This project is licensed under the MIT License.

```plaintext
MIT License

Copyright (c) 2024 G4UR4V007

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Author
- **G4UR4V007**

## Version
- 1.0
