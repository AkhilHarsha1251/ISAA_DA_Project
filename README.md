# File Encryptor/Decryptor (ISAA Project)

This is a Python script that encrypts and decrypts files using the Camellia block cipher in CFB mode. It uses the `cryptography` library for encryption/decryption and key derivation.

## Requirements
- Python 3.x
- `cryptography` library

## Usage
1. Run the script
2. Click the "Encrypt File" button to encrypt a file
3. Select the input file to be encrypted
4. Enter a password to derive a key for encryption
5. Select a location to save the encrypted file
6. The salt and IV used for encryption will be saved to separate files with the same name as the output file, but with `.salt` and `.iv` extensions respectively.
7. Click the "Decrypt File" button to decrypt a file
8. Select the encrypted file to be decrypted
9. Enter the password used for encryption
10. Select a location to save the decrypted file
11. The salt and IV used for encryption will be loaded from the corresponding `.salt` and `.iv` files in the same directory as the encrypted file.

Note: If you enter the wrong password more than 5 times, the program will exit.

Sure! Here's an example of how you could include the installation instructions in the README:

## Installation
1. Clone the repository or download the ZIP file and extract it to a directory of your choice.
2. Install the `cryptography` library using pip:
```
pip install cryptography
```
3. Run the script using Python 3.x:
```
python final.py
``` 
Note: The script has been tested on Windows and Linux operating systems. If you encounter any issues running the script, please let me know.

For Windows Operating Systems Just the Run [final.exe](https://github.com/AkhilHarsha1251/ISAA_DA_Project/blob/main/Windows%20Package%20Files/dist/final.exe) file
```
final.exe
``` 
## Limitations
- Only supports files encrypted with this script
- Does not support batch encryption/decryption of multiple files at once

## How it works
The script uses the `PBKDF2HMAC` key derivation function to derive a 256-bit key from the user's password and a randomly generated 128-bit salt. It then generates a 128-bit IV and initializes a Camellia cipher in CFB mode with the key and IV. The input file is read in, padded with PKCS7 padding to a multiple of the block size, and encrypted using the cipher. The salt and IV are saved to separate files with the same name as the output file, but with `.salt` and `.iv` extensions respectively.

To decrypt a file, the script prompts the user for the password used to encrypt the file. It loads the salt and IV from the corresponding `.salt` and `.iv` files in the same directory as the encrypted file, derives the key using the same password and salt, initializes a Camellia cipher in CFB mode with the key and IV, and decrypts the file.

## Security considerations
The `cryptography` library is a widely used and trusted library for encryption/decryption and key derivation. However, it is important to note that this script is not intended for use in high-security applications, as it has not undergone a formal security audit and may contain vulnerabilities. Additionally, the security of the encryption depends on the strength of the user's password and the randomness of the salt and IV. Users should choose strong passwords and ensure that the salt and IV are generated using a cryptographically secure random number generator.

## Developed by
This script was developed by [Akili Harsha Vardhan](). If you have any questions or feedback, please feel free to contact me at akhilharsha78@gmail.com. Contributions are also welcome - if you would like to contribute to the project, please create a pull request or contact me directly.

## Acknowledgements
This script was developed as part of a project by [Harsha Vardhan, Srujay, Aadhyanth, Srinandhan]() for the Information Security and Assurance Architecture (ISAA) course at [Vellore Institute of Technology](https://vit.ac.in/). The authors would like to thank [Dr. Priyadarshini R](https://chennai.vit.ac.in/member/dr-priyadarshini-ramasubramanian/) for their guidance and support throughout the project.
