def main():
    A, B = map(int, input().split())
    if 1 <= A <= 20 and 1 <= B <= 20:
        print(A * B)
    else:
        print(-1)
