# Brute-Force Hash Cracking Tool

## Description

This is a Python-based brute-force hash-cracking tool that aims to identify plaintext passwords from various hash values. The tool is still in development, and additional features may be added in future versions.

## Features

- **Supports multiple hash types**:
  - MD5 (32 characters)
  - SHA1 (40 characters)
  - SHA256 (64 characters)
  - SHA512 (128 characters)
  
- **Customizable character sets**, allowing the user to include:
  - Numbers (`n`)
  - Lowercase letters (`l`)
  - Uppercase letters (`u`)
  - Special characters (`s`)
  
- **Option to specify minimum and maximum password lengths.**
  
- **Progress indicator** to show the percentage of combinations tried.
  
- **Simple command-line interface** for user interaction.

## Requirements

- Python 3.x
- `hashlib` (included in Python standard library)
- `itertools` (included in Python standard library)
- `string` (included in Python standard library)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pranay-root/brutehash.git
   cd brutehash
   ```
2. Install Dependencies: Make sure you have Python installed. The required libraries are part of the Python standard library, so no additional installations are needed.

## Usage

- Run the Tool:
  ```
  python3 brutehash.py or python3 brutehashfast.py
  ```
- Follow the Prompts:
  ```
  Enter the hash you want to crack.
  Choose your character set (e.g., n, l, u, s, or combinations like nl, lu, etc.).
  Specify the minimum and maximum password lengths.
  View Progress: The tool will display the progress percentage as it tries to crack the hash.
  ```

## Contributing
- If you would like to contribute to this project, please fork the repository and submit a pull request. Any enhancements or bug fixes are welcome.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.
  
