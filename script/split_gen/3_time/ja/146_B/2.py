def main():
    N = int(input())
    S = input()
    for s in S:
        print(chr(ord('A') + (ord(s) - ord('A') + N) % 26), end='')
