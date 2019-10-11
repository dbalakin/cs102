def encrypt_caesar(plaintext: str) -> str:
    """
        >>> encrypt_caesar("PYTHON")
        'SBWKRQ'
        >>> encrypt_caesar("python")
        'sbwkrq'
        >>> encrypt_caesar("Python3.6")
        'Sbwkrq3.6'
        >>> encrypt_caesar("")
        ''
        """
    # PUT YOUR CODE HERE
    ciphertext = ""
    for i in plaintext:
        if 65 <= ord(i) <= 90:
            if ord(i) + 3 > ord("Z"):
                ciphertext += chr(ord(i) + 3 - 26)
            else:
                ciphertext += chr(ord(i) + 3)
        elif 97 <= ord(i) <= 122:
            if ord(i) + 3 > ord("z"):
                ciphertext += chr(ord(i) + 3 - 26)
            else:
                ciphertext += chr(ord(i) + 3)
        else:
            ciphertext += i
    return ciphertext

def decrypt_caesar(ciphertext: str) -> str:
    """
        >>> decrypt_caesar("SBWKRQ")
        'PYTHON'
        >>> decrypt_caesar("sbwkrq")
        'python'
        >>> decrypt_caesar("Sbwkrq3.6")
        'Python3.6'
        >>> decrypt_caesar("")
        ''
        """
    # PUT YOUR CODE HERE
    plaintext = ""
    for i in ciphertext:
        if 65 <= ord(i) <= 90:
            if ord(i) - 3 < ord("A"):
                plaintext += chr(ord(i) - 3 + 26)
            else:
                plaintext += chr(ord(i) - 3)
        elif 97 <= ord(i) <= 122:
            if ord(i) - 3 < ord("a"):
                plaintext += chr(ord(i) - 3 + 26)
            else:
                plaintext += chr(ord(i) - 3)
        else:
            plaintext += i
    return plaintext