def f(X):
    if X < 50:
        return 0
    elif X >= 50 and X < 100:
        return 1
    elif X >= 100 and X < 150:
        return 2
    elif X >= 150 and X < 200:
        return 3
    elif X >= 200 and X < 250:
        return 4
    elif X >= 250 and X < 300:
        return 5
    elif X >= 300 and X < 350:
        return 6
    elif X >= 350 and X < 400:
        return 7
    elif X >= 400 and X < 450:
        return 8
    elif X >= 450 and X < 500:
        return 9
    elif X >= 500 and X < 550:
        return 10
    elif X >= 550 and X < 600:
        return 11
    elif X >= 600 and X < 650:
        return 12
    elif X >= 650 and X < 700:
        return 13
    elif X >= 700 and X < 750:
        return 14
    elif X >= 750 and X < 800:
        return 15
    elif X >= 800 and X < 850:
        return 16
    elif X >= 850 and X < 900:
        return 17
    elif X >= 900 and X < 950:
        return 18
    elif X >= 950 and X < 1000:
        return 19
    elif X >= 1000:
        return 20
n = int(input())
s = input()
w = list(map(int,input().split()))
ans = 0
for i in range(n):
    if s[i] == '1':
        ans += f(w[i])
print(ans)

if __name__ == '__main__':
    f()