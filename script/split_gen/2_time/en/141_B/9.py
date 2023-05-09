def main():
    print('Yes' if all([s[::2].count('R') == 0, s[1::2].count('L') == 0]) else 'No')
