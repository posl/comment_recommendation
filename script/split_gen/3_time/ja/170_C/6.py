def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
    else:
        p = list(map(int, input().split()))
        p.sort()
        #print(p)
        if X < p[0]:
            print(p[0])
        elif X > p[-1]:
            print(p[-1])
        else:
            for i in range(N):
                if p[i] <= X < p[i+1]:
                    if X - p[i] <= p[i+1] - X:
                        print(p[i])
                    else:
                        print(p[i+1])
                    break
