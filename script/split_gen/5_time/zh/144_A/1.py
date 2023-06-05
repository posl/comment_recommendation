def main():
    A, B = map(int, input().split())
    if (A > 0 and A < 21) and (B > 0 and B < 21):
        print(A * B)
    else:
        print(-1)
