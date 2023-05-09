def main():
    N = int(input())
    p = []
    for i in range(0,N):
        p.append(int(input()))
    p.sort()
    p[N-1] = int(p[N-1] / 2)
    print(sum(p))
