def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min_count = 1000000
    max_count = 0
    for i in range(1,w+1):
        if a*i <= w and w <= b*i:
            min_count = min(min_count, i)
            max_count = max(max_count, i)
    if min_count == 1000000:
        print("UNSATISFIABLE")
    else:
        print(min_count, max_count)

if __name__ == '__main__':
    main()