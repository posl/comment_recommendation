def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        while l+i<N and S[l]!=S[l+i]:
            l+=1
        print(l)

if __name__ == '__main__':
    main()