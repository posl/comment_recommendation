def main():
    n = int(input())
    x = list(map(int, input().split()))
    for i in range(3):
        if i == 0:
            ans = sum([abs(x[j]) for j in range(n)])
        elif i == 1:
            ans = sum([x[j]**2 for j in range(n)])**(1/2)
        elif i == 2:
            ans = max([abs(x[j]) for j in range(n)])
        print(ans)

if __name__ == '__main__':
    main()