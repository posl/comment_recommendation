def main():
    N, A, B = map(int, input().split())
    blue = N//(A+B)
    remain = N%(A+B)
    if remain <= A:
        print(blue*A+remain)
    else:
        print(blue*A+A)
