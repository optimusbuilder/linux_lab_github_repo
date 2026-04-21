import sys

def main():
    # Get shift key from command-line argument
    shift = int(sys.argv[1]) % 26

    # Read all input from stdin
    text = ""
    for line in sys.stdin:
        text += line

    # Convert to uppercase and keep only A–Z
    cleaned = ""
    for ch in text.upper():
        if 'A' <= ch <= 'Z':
            cleaned += ch

    # Encode using Caesar cipher
    encoded = ""
    for ch in cleaned:
        encoded += chr(((ord(ch) - ord('A') + shift) % 26) + ord('A'))

    # Break into blocks of 5 letters
    blocks = []
    for i in range(0, len(encoded), 5):
        blocks.append(encoded[i:i+5])

    # Print 10 blocks per line
    for i in range(0, len(blocks), 10):
        print(" ".join(blocks[i:i+10]))

if __name__ == "__main__":
    main()
