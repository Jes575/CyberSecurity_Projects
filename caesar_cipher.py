import sys

if len(sys.argv) == 1:
    print("Usage: " +str(sys.argv[0] +"[encrypt/decrypt] [message]"))
    sys.exit()

mode = sys.argv[1]

message = sys.argv[2]

key = 13

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 !?.'

resultText = ''

for letter in message:
    if letter in ALPHABET:
        letterIndex = ALPHABET.find(letter)
        if mode == 'encrypt':
            resultIndex = letterIndex + key
        elif mode == 'decrypt':
            resultIndex = letterIndex - key
        if resultIndex >= len(ALPHABET):
            resultIndex = resultIndex - len(ALPHABET)
        elif resultIndex < 0:
            resultIndex = resultIndex + len(ALPHABET)
        resultText = resultText + ALPHABET[resultIndex]
    else:
            resultText = resultText + letter

print(resultText)

