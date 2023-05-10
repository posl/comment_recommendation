def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    min = max(a)
    max = min(b)
    if min > max:
        print(0)
    else:
        print(max - min + 1)

if __name__ == '__main__':
    main()