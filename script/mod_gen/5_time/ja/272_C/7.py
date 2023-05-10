def main():
    N = int(input())
    A = list(map(int, input().split()))
    odd = []
    even = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) == 0:
        print(-1)
    else:
        print(sum(even) + max(odd))

if __name__ == '__main__':
    main()