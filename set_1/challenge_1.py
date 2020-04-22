import base64
from hexbytes import HexBytes

def encode_base64(ascii_string):
    binary = ''.join(
        format(ord(symbol), '08b')
        for symbol in ascii_string
    )
    extra_zeros = (6 - len(binary) % 6) % 6
    binary += '0' * extra_zeros
    sextets = [binary[i:i + 6] for i in range(0, len(binary), 6)]
    chars = []
    for sextet in sextets:
        value = int(sextet, 2)
        if value < 26:
            chars.append(chr(ord('A') + value))
        elif value < 26 * 2:
            chars.append(chr(ord('a') + value - 26))
        elif value < 26 * 2 + 10:
            chars.append(chr(ord('0') + value - 26 * 2))
        elif value == 62:
            chars.append('+')
        elif value == 63:
            chars.append('/')
        else:
            raise TypeError('wtf')
    padding_size = (3 - len(ascii_string) % 3) % 3
    return ''.join(chars) + '=' * padding_size


if __name__ == '__main__':
    inputs = [
        HexBytes('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d').decode(),
        'Man',
        'pleasure.',
        'leasure.',
        'easure.',
        'asure.',
        'sure.',
    ]
    for input in inputs:
        print(input, encode_base64(input), base64.b64encode(input.encode()))
