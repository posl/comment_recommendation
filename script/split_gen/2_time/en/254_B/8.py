def main():
    def pascal(N):
        if N == 0:
            return [1]
        else:
            p = pascal(N-1)
            return [1] + [p[i]+p[i+1] for i in range(len(p)-1)] + [1]
    N = int(input())
    for i in range(N):
        print(" ".join(map(str, pascal(i))))
