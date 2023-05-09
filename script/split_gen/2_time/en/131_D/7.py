def main():
    #input
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #compute
    jobs = []
    for i in range(N):
        jobs.append([A[i], B[i]])
    jobs.sort(key=lambda x: x[1])
    time = 0
    for a, b in jobs:
        time += a
        if time > b:
            print('No')
            return
    print('Yes')
