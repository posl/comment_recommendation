def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L2 <= R1:
        if R2 <= R1:
            print(R2 - L2)
        else:
            print(R1 - L2)
    else:
        print(0)
