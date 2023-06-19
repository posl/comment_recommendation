def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    time = [0] * n
    time[0] = t[0]
    for i in range(1, n):
        if time[i-1] + s[i-1] > t[i]:
            time[i] = time[i-1] + s[i-1]
        else:
            time[i] = t[i]
    for i in range(n):
        print(time[i])

if __name__ == '__main__':
    main()