def main():
    n = int(input())
    time = []
    for i in range(n):
        time.append(list(map(int, input().split())))
    print(time)
    ans = 0
    for i in range(n):
        if i == n-1:
            ans += time[i][2]
        else:
            if time[i][1] == time[i+1][1]:
                if time[i][2] >= time[i+1][2]:
                    ans += time[i][2]
                else:
                    ans += time[i+1][2]
    print(ans)

if __name__ == '__main__':
    main()