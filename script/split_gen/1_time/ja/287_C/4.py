def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    else:
        for i in range(M):
            u, v = map(int, input().split())
            if abs(u-v) != 1:
                print("No")
                return
        print("Yes")
        return
