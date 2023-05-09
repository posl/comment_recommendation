def main():
    N, M = map(int, input().split())
    a = M // N
    if M % N == 0:
        print(a)
    else:
        print(a - 1)
