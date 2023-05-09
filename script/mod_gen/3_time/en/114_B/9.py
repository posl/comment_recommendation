def main():
    S = input()
    S = int(S)
    S = str(S)
    S = S.zfill(10)
    S = list(S)
    S = [int(s) for s in S]
    S = sorted(S)
    S = [str(s) for s in S]
    S = ''.join(S)
    S = int(S)
    if S < 753:
        print(753 - S)
    elif S >= 753:
        print(S - 753)

if __name__ == '__main__':
    main()