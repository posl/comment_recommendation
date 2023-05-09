def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        Sushi.append([d, t])
    Sushi.sort(reverse=True)
    Sushi = Sushi[:K]
    Sushi.sort(key=lambda x:x[1])
    Sushi2 = Sushi[:]
    Sushi2.sort()
    Sushi3 = Sushi[:]
    Sushi3.sort(key=lambda x:x[0], reverse=True)
    ans = 0
    for i in range(K):
        ans += Sushi[i][0]
    ans += (len(set(Sushi))**2)
    for i in range(K):
        if len(set(Sushi2)) == K:
            break
        if Sushi2[i][1] not in set(Sushi2[:i]):
            Sushi2.append(Sushi2[i])
            Sushi2.sort(key=lambda x:x[1])
            Sushi2.sort(key=lambda x:x[0], reverse=True)
            Sushi2 = Sushi2[:K]
            ans2 = 0
            for j in range(K):
                ans2 += Sushi2[j][0]
            ans2 += (len(set(Sushi2))**2)
            if ans2 > ans:
                ans = ans2
    for i in range(K):
        if len(set(Sushi3)) == K:
            break
        if Sushi3[i][1] not in set(Sushi3[:i]):
            Sushi3.append(Sushi3[i])
            Sushi3.sort(key=lambda x:x[1])
            Sushi3.sort(key=lambda x:x[0], reverse=True)
            Sushi3 = Sushi3[:K]
            ans3 = 0
            for j in range(K):
                ans3 += Sushi3[j][0]
            ans3 += (len(set(Sushi3))**2)
            if ans3 > ans:
                ans = ans3
    print(ans)

if __name__ == '__main__':
    main()