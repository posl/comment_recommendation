def main():
    n = int(input())
    l = list(map(int,input().split()))
    max = l[0]
    sum = 0
    for i in l:
        if i > max:
            max = i
        sum += i
    if max < sum - max:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()