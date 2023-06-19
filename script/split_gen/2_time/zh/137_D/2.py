def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for i in range(N)]
    jobs.sort(key=lambda x:x[0])
    ans = 0
    i = 0
    while i < N:
        if M >= jobs[i][0]:
            ans += jobs[i][1]
            M -= 1
        else:
            break
        i += 1
    print(ans)
