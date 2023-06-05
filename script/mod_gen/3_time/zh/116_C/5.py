def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    count = 0
    while sum(h) > 0:
        count += 1
        i = 0
        while i < n:
            if h[i] > 0:
                j = i
                while j < n and h[j] > 0:
                    h[j] -= 1
                    j += 1
                break
            i += 1
    print(count)

if __name__ == '__main__':
    main()