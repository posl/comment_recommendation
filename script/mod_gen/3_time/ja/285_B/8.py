def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        s = S[:i]
        t = S[i:]
        l = 0
        for j in range(1,len(s)+1):
            if s[-j] != t[-j]:
                l = j
                break
        print(l)

if __name__ == '__main__':
    main()