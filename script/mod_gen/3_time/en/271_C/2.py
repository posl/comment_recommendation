def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    if n == 1:
        if a[0] == 1:
            print(1)
        else:
            print(0)
        return
    a.sort()
    if a[0] != 1:
        print(0)
        return
    max_volume = 1
    for i in range(1, n):
        if a[i] == max_volume + 1:
            max_volume += 1
        elif a[i] > max_volume + 1:
            break
    print(max_volume)

if __name__ == '__main__':
    main()