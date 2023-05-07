def main():
    N, A, B = map(int, input().split())
    print(N*(N+1)//2 - (N//A+A*(N//A-1)*N//2//A) - (N//B+B*(N//B-1)*N//2//B) + (N//A//B+A*B*(N//A//B-1)*N//2//(A*B)))

if __name__ == '__main__':
    main()