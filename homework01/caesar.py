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
    ciphertext = ""
    for ch in plaintext:
        if "A" <= ch <= "Z":
            if ord(ch) + 3 > "Z":
                ciphertext += chr(ord(ch) + 3 - 26)
            else:
                ciphertext += chr(ord(ch) + 3)
        elif "a" <= ch <= "z":
            if ord(ch) + 3 > "z":
                ciphertext += chr(ord(ch) + 3 - 26)
            else:
                ciphertext += chr(ord(ch) + 3)
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
    plaintext = ""
    for ch in ciphertext:
        if "A" <= ch <= "Z":
            if ord(ch) - 3 < "A":
                plaintext += chr(ord(ch) - 3 + 26)
            else:
                plaintext += chr(ord(ch) - 3)
        elif "a" <= ch <= "z":
            if ord(ch) - 3 < "a":
                plaintext += chr(ord(ch) - 3 + 26)
            else:
                plaintext += chr(ord(ch) - 3)
        else:
            plaintext += ch
    return plaintext
