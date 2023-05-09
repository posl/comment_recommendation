def main():
    A, B, T = map(int, input().split())
    if T < A:
        print('0')
    else:
        print(B * (T // A))
