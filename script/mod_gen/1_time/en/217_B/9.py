def main():
    # S_1 = input()
    # S_2 = input()
    # S_3 = input()
    S_1, S_2, S_3 = input().split()
    S = ['ABC', 'ARC', 'AGC', 'AHC']
    S.remove(S_1)
    S.remove(S_2)
    S.remove(S_3)
    print(S[0])

if __name__ == '__main__':
    main()