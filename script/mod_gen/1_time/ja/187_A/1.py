def main():
    A, B = map(int, input().split())
    S_A = sum(int(i) for i in str(A))
    S_B = sum(int(i) for i in str(B))
    print(max(S_A, S_B))

if __name__ == '__main__':
    main()