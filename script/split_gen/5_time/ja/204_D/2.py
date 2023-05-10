def main():
    N = int(input())
    T = [int(i) for i in input().split()]
    T.sort()
    #print(T)
    ans = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0
    ans5 = 0
    ans6 = 0
    ans7 = 0
    ans8 = 0
    ans9 = 0
    for i in range(N):
        if i % 9 == 0:
            ans += T[i]
        elif i % 9 == 1:
            ans2 += T[i]
        elif i % 9 == 2:
            ans3 += T[i]
        elif i % 9 == 3:
            ans4 += T[i]
        elif i % 9 == 4:
            ans5 += T[i]
        elif i % 9 == 5:
            ans6 += T[i]
        elif i % 9 == 6:
            ans7 += T[i]
        elif i % 9 == 7:
            ans8 += T[i]
        elif i % 9 == 8:
            ans9 += T[i]
    print(max(ans, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9))
