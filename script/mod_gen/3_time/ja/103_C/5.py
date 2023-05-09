def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)
    max_list = []
    for i in range(n):
        max_list.append(a_list[i]*(n-i))
    print(max(max_list))

if __name__ == '__main__':
    main()