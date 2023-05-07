def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    else:
        u = [0] * M
        v = [0] * M
        for i in range(M):
            u[i], v[i] = map(int, input().split())
        if len(set(u)) == len(set(v)) == N:
            print("Yes")
        else:
            print("No")
