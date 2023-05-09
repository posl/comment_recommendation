def main():
    A, B = map(int, input().split())
    if A < 1 or A > 20 or B < 1 or B > 20:
        return
    print(A*B) if A <= 9 and B <= 9 else print(-1)
