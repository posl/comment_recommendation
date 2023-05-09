def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    for i in range(M):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        if u == 1 and v == N:
            continue
        if u != i + 1 or v != i + 2:
            print("No")
            return
    print("Yes")
