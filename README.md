# Caesar Cipher Encoder

A simple command-line tool that encodes text using the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher). It reads plain text from standard input, strips non-alphabetic characters, applies a configurable letter shift, and prints the result formatted in classic 5-letter cipher blocks.

---

## Usage

```bash
python caesar.py <shift> < input.txt
```

Or pipe text directly:

```bash
echo "Hello, World!" | python caesar.py 3
```

### Arguments

| Argument | Description |
|----------|-------------|
| `shift`  | Integer specifying how many positions to shift each letter (e.g. `3` shifts A→D). Values are automatically wrapped modulo 26. |

### Input

- Plain text read from **stdin** (a file redirect or pipe).
- Any character that is not a letter (A–Z, a–z) is silently ignored.
- Input is case-insensitive; everything is converted to uppercase before encoding.

### Output

- Encoded uppercase letters printed in **groups of 5**, with **10 groups per line**.

---

## Example

```bash
echo "Attack at dawn!" | python caesar.py 13
```

**Output:**
```
NGGNP XNGQN JA
```

---

## How It Works

1. **Read** — All text is read from stdin.
2. **Clean** — Input is uppercased and all non-alphabetic characters are removed.
3. **Encode** — Each letter is shifted forward by `shift` positions (wrapping Z → A).
4. **Format** — The encoded string is split into 5-letter blocks, 10 per line.

The shift value is taken modulo 26, so a shift of `29` behaves the same as a shift of `3`.

---

## Requirements

- Python 3.x
- No external dependencies

---

## Decoding

To decode a message, shift by the **inverse** amount (`26 - shift`):

```bash
# Encoded with shift 3 → decode with shift 23
echo "NGGNP XNGQN JA" | python caesar.py 23
```

---

## Limitations

- Only encodes the 26 English letters (A–Z); digits, punctuation, and spaces are dropped.
- Output format (5-letter blocks) follows traditional cipher conventions and does not preserve the original word boundaries.
