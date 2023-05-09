def main():
    N, A, B = map(int, input().split())
    print(N*(N+1)//2 - (A*(N//A)*(N//A+1)//2 + B*(N//B)*(N//B+1)//2 - A*B*(N//(A*B))*(N//(A*B)+1)//2))

if __name__ == '__main__':
    main()