def harvest():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i > 10:
            count += i - 10
    print(count)

if __name__ == '__main__':
    harvest()