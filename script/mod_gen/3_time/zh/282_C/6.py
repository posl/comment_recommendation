def main():
    N = input()
    S = input()
    S = list(S)
    for i in range(0,len(S),2):
        S[i] = '.'
    print(''.join(S))

if __name__ == '__main__':
    main()