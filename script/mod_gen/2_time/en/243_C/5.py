def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    s = input()
    ans = 'No'
    for i in range(n):
        if s[i] == 'R':
            for j in range(n):
                if i != j and s[j] == 'L':
                    if x[i] < x[j] and y[i] == y[j]:
                        ans = 'Yes'
                        break
        if ans == 'Yes':
            break
    print(ans)

if __name__ == '__main__':
    main()