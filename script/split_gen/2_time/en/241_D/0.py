def main():
    N = int(input())
    A = []
    for _ in range(N):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A.append(q[1])
        elif q[0] == 2:
            B = [a for a in A if a <= q[1]]
            if len(B) >= q[2]:
                print(sorted(B, reverse=True)[q[2]-1])
            else:
                print(-1)
        elif q[0] == 3:
            B = [a for a in A if a >= q[1]]
            if len(B) >= q[2]:
                print(sorted(B)[q[2]-1])
            else:
                print(-1)
