def main():
    S = [input() for _ in range(3)]
    T = input()
    for c in T:
        print(S[int(c)-1], end='')
    print()
