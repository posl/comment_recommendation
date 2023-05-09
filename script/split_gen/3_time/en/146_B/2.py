def main():
    n = int(input())
    s = input()
    for c in s:
        if ord(c) + n > ord('Z'):
            print(chr(ord(c) + n - 26), end='')
        else:
            print(chr(ord(c) + n), end='')
