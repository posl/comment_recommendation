def main():
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list.sort(reverse=True)
    print(A_list[K - 1])

if __name__ == '__main__':
    main()