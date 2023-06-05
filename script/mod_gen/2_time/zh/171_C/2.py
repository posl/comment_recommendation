def main():
    N, K = map(int, input().split())
    p_list = list(map(int, input().split()))
    p_list.sort()
    print(sum(p_list[:K]))

if __name__ == '__main__':
    main()