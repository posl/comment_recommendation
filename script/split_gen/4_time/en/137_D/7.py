def main():
    N,M = map(int,input().split())
    jobs = []
    for i in range(N):
        A,B = map(int,input().split())
        jobs.append((A,B))
    jobs.sort()
    jobs.reverse()
    reward = 0
    for i in range(1,M+1):
        while jobs and jobs[-1][0] <= i:
            reward += jobs[-1][1]
            jobs.pop()
    print(reward)
