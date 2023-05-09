def main():
    N, K = map(int, input().split())
    print(len(str(N))) if K == 10 else print(len(change_base(N, K)))

if __name__ == '__main__':
    main()