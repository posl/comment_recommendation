def main():
    A, B = map(int, input().split())
    print(max(A*2-1, B*2-1, A+B))

if __name__ == '__main__':
    main()