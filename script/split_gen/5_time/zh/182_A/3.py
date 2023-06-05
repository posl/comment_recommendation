def main():
    A, B = map(int, input().split())
    if B <= 2*A+100:
        print(2*A+100-B)
    else:
        print(0)
