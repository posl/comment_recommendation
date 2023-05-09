def main():
    N = int(input())
    S = input()
    for s in S:
        print(chr((ord(s) - ord('A') + N) % 26 + ord('A')), end='')
    print()
