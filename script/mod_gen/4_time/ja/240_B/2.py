def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    a_set = set(a_list)
    print(len(a_set))

if __name__ == '__main__':
    main()