def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = set([S1,S2,S3])
    S4 = set(['ABC','ARC','AGC','AHC'])
    print(S4.difference(S).pop())

if __name__ == '__main__':
    main()