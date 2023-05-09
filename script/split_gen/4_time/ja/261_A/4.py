def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 <= L2 and R1 >= L2:
        print(min(R1, R2) - L2)
    elif L1 <= R2 and R1 >= R2:
        print(R2 - max(L1, L2))
    else:
        print(0)
