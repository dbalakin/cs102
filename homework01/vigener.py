def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
        >>> encrypt_vigenere("PYTHON", "A")
        'PYTHON'
        >>> encrypt_vigenere("python", "a")
        'python'
        >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
        'LXFOPVEFRNHR'
        """
    # PUT YOUR CODE HERE
    ciphertext = ""
    keyword *= len(plaintext) // len(keyword) + 1
    for i, j in enumerate(plaintext):
        if 65 <= ord(j) <= 90:
            if (ord(keyword[i]) - 65) + ord(j) > 90:
                ciphertext += chr((ord(keyword[i]) - 65) + ord(j)-26)
            else:
                ciphertext += chr((ord(keyword[i]) - 65) + ord(j))

        elif 97 <= ord(j) <= 122:
                if (ord(keyword[i]) - 97) + ord(j) > 122:
                    ciphertext  += chr(((ord(keyword[i]) - 97) + ord(j) - 26))
                else:
                    ciphertext += chr((ord(keyword[i]) - 97) + ord(j))
        else:
            ciphertext += j
    return


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
        >>> decrypt_vigenere("PYTHON", "A")
        'PYTHON'
        >>> decrypt_vigenere("python", "a")
        'python'
        >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
        'ATTACKATDAWN'
        """
    # PUT YOUR CODE HERE
    plaintext = ""
    keyword *= len(ciphertext) // len(keyword) + 1
    for i, j in enumerate(ciphertext):
        if 65 <= ord(j) <= 90:
            if (ord(j) - (ord(keyword[i]) - 65)) < 65:
                plaintext += chr(ord(j)-(ord(keyword[i]) - 65) + 26)
            else:
                plaintext += chr(ord(j) - (ord(keyword[i]) - 65))
        elif 97 <= ord(j) <= 122:
                if (ord(j) - (ord(keyword[i]) - 97)) < 97:
                    plaintext += chr((ord(j) - (ord(keyword[i]) - 97) + 26))
                else:
                    plaintext += chr(ord(j) - (ord(keyword[i]) - 97))
        else:
            plaintext += j

    return plaintext