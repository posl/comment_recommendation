def main():
    S = []
    for i in range(3):
        S.append(input())
    for c in ["ABC", "ARC", "AGC", "AHC"]:
        if c not in S:
            print(c)
            break

if __name__ == '__main__':
    main()