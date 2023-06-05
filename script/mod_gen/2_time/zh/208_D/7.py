def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    a_sorted.append(a_sorted[0]+k)
    for i in range(n):
        if a_sorted[i+1] == a_sorted[i]:
            print(k//n)
        else:
            print(k//n+1)

if __name__ == '__main__':
    main()