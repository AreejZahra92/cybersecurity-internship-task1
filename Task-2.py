"""
DecodeLabs Cybersecurity Internship - Project 2
Basic Encryption & Decryption (Caesar Cipher)

Goal: Implement a simple, reversible encryption technique that:
  1. Encrypts user text using a shift-based logic
  2. Decrypts the encrypted text back to the original
  3. Displays both encrypted and decrypted output
  4. Handles edge cases (spaces, punctuation, numbers, lowercase/uppercase)
"""


def encrypt(text: str, shift: int) -> str:
    """
    Encrypts plaintext using the Caesar Cipher formula:
        E(x) = (x + n) % 26

    Each letter is shifted forward by 'shift' positions in the alphabet.
    Non-letter characters (spaces, punctuation, digits) are left unchanged.
    """
    result = []

    for char in text:
        if char.isupper():
            # Normalize to 0-25, shift, wrap with modulo, convert back to ASCII
            shifted = (ord(char) - ord('A') + shift) % 26
            result.append(chr(shifted + ord('A')))
        elif char.islower():
            shifted = (ord(char) - ord('a') + shift) % 26
            result.append(chr(shifted + ord('a')))
        else:
            # Edge case: spaces, punctuation, numbers stay the same
            result.append(char)

    return ''.join(result)


def decrypt(cipher_text: str, shift: int) -> str:
    """
    Decrypts ciphertext using the reverse Caesar Cipher formula:
        D(x) = (x - n) % 26

    This is symmetric encryption: the SAME key (shift) that locked
    the data is used to unlock it, just applied in reverse.
    """
    # Decryption is just encryption with a negative shift
    return encrypt(cipher_text, -shift)


def main():
    print("=" * 50)
    print("  DECODELABS - CAESAR CIPHER TOOL")
    print("=" * 50)

    # Step 1: Get plaintext input from the user
    plaintext = input("\nEnter the text you want to encrypt: ")

    # Step 2: Get the shift key from the user (bonus: custom key, not hardcoded)
    while True:
        try:
            shift = int(input("Enter the shift key (e.g. 3): "))
            break
        except ValueError:
            print("Please enter a valid whole number for the shift key.")

    # Step 3: Encrypt
    encrypted_text = encrypt(plaintext, shift)

    # Step 4: Decrypt (to prove the process is reversible)
    decrypted_text = decrypt(encrypted_text, shift)

    # Step 5: Display everything clearly
    print("\n--- RESULTS ---")
    print(f"Original Text   : {plaintext}")
    print(f"Shift Key Used  : {shift}")
    print(f"Encrypted Text  : {encrypted_text}")
    print(f"Decrypted Text  : {decrypted_text}")

    # Step 6: Validation check
    if decrypted_text == plaintext:
        print("\n[SUCCESS] Decrypted text matches the original. Logic verified!")
    else:
        print("\n[ERROR] Mismatch detected. Check your shift logic.")


if __name__ == "__main__":
    main()