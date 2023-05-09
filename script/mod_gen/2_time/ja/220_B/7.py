def main():
    K = int(input())
    A,B = map(str,input().split())
    ans = int(A,K)*int(B,K)
    print(ans)

if __name__ == '__main__':
    main()