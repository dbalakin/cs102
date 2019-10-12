def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for ch in plaintext:
        if "A" <= ch <= "Z":
            if ch + 3 > "Z":
                ciphertext += chr(ch + 3 - 26)
            else:
                ciphertext += chr(ch + 3)
        elif "a" <= ch <= "z":
            if ch + 3 > "z":
                ciphertext += chr(ch + 3 - 26)
            else:
                ciphertext += chr(ch + 3)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for ch in ciphertext:
        if "A" <= ch <= "Z":
            if ch - 3 < "A":
                plaintext += chr(ch - 3 + 26)
            else:
                plaintext += chr(ch - 3)
        elif "a" <= ch <= "z":
            if ch - 3 < "a":
                plaintext += chr(ch - 3 + 26)
            else:
                plaintext += chr(ch - 3)
        else:
            plaintext += i
    return plaintext
