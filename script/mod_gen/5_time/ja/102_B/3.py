def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_max = max(a_list)
    a_min = min(a_list)
    print(a_max - a_min)

if __name__ == '__main__':
    main()