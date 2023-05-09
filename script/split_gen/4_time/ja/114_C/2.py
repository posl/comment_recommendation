def solve():
    N = int(input())
    ans = 0
    for i in range(3, 10):
        for j in range(3, 10):
            for k in range(3, 10):
                if i == 3 and j == 5 and k == 7:
                    ans += 1
                elif i == 3 and j == 7 and k == 5:
                    ans += 1
                elif i == 5 and j == 3 and k == 7:
                    ans += 1
                elif i == 5 and j == 7 and k == 3:
                    ans += 1
                elif i == 7 and j == 3 and k == 5:
                    ans += 1
                elif i == 7 and j == 5 and k == 3:
                    ans += 1
    print(ans)
