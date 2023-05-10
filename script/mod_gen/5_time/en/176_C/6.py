def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_height = 0
    answer = 0
    for i in range(n):
        if a[i] >= max_height:
            max_height = a[i]
        else:
            answer += max_height - a[i]
    print(answer)

if __name__ == '__main__':
    main()