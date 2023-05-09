def main():
    A, B, C, D = map(int, input().split())
    if A <= B*C*D:
        print((B*C*D-A+D-1)//(B*D))
    else:
        print(-1)
