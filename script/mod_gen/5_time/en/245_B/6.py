def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for a in A:
        if a == count:
            count += 1
        elif a > count:
            break
    print(count)
main()

if __name__ == '__main__':
    main()