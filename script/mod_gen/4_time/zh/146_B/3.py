def main():
    N = int(input())
    S = input()
    L = list(S)
    for i in range(len(L)):
        L[i] = chr(((ord(L[i])-ord('A'))+N)%26 + ord('A'))
    print(''.join(L))

if __name__ == '__main__':
    main()