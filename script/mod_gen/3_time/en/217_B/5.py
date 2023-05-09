def main():
    S = []
    for i in range(3):
        S.append(input())
    for i in ['ABC', 'ARC', 'AGC', 'AHC']:
        if i not in S:
            print(i)

if __name__ == '__main__':
    main()