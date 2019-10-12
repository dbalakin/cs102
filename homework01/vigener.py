def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword *= len(plaintext) // len(keyword) + 1
    for i, pl in enumerate(plaintext):
        if "A" <= pl <= "Z":
            if (ord(keyword[i]) - ord("A")) + ord(pl) > ord("Z"):
                ciphertext += chr((ord(keyword[i]) - ord("A")) + ord(pl)-26)
            else:
                ciphertext += chr((ord(keyword[i]) - ord("A")) + ord(pl))
        elif "a" <= pl <= "z":
            if (ord(keyword[i]) - ord("a")) + ord(j) > ord("z"):
                ciphertext  += chr(((ord(keyword[i]) - ord("a")) + ord(pl) - 26))
            else:
                ciphertext += chr((ord(keyword[i]) - ord("a")) + ord(pl))
        else:
            ciphertext += pl
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword *= len(ciphertext) // len(keyword) + 1
    for i, ci in enumerate(ciphertext):
        if "A" <= ci <= "Z":
            if (ord(ci) - (ord(keyword[i]) - ord("A"))) < ord("A"):
                plaintext += chr(ord(ci)-(ord(keyword[i]) - ord("A")) + 26)
            else:
                plaintext += chr(ord(ci) - (ord(keyword[i]) - ord("A")))
        elif "a" <= ord(ci) <= "z":
            if (ord(ci) - (ord(keyword[i]) - ord("a"))) < ord("a"):
                plaintext += chr((ord(ci) - (ord(keyword[i]) - ord("a")) + 26))
            else:
                plaintext += chr(ord(ci) - (ord(keyword[i]) - ord("a")))
        else:
            plaintext += ci
    return plaintext
