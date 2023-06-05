def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1 / a_list[i]
    print(1 / sum)

if __name__ == '__main__':
    main()