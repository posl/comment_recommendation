def main():
    K = int(input())
    A,B = map(int,input().split())
    print(int(str(A),K)*int(str(B),K))

if __name__ == '__main__':
    main()