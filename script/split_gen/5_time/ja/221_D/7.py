def main():
    N = int(input())
    login = []
    for i in range(N):
        a, b = map(int, input().split())
        login.append([a, b])
    login.sort()
    max_day = 0
    for i in range(N):
        if login[i][0] + login[i][1] > max_day:
            max_day = login[i][0] + login[i][1]
    #print(max_day)
    login_day = [0] * (max_day + 1)
    for i in range(N):
        login_day[login[i][0]] += 1
        login_day[login[i][0] + login[i][1]] -= 1
    #print(login_day)
    for i in range(1, max_day + 1):
        login_day[i] += login_day[i - 1]
    for i in range(1, max_day + 1):
        print(login_day[i], end=" ")
    print()
