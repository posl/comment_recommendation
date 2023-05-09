def main():
    A, B = map(int, input().split())
    if A < 6:
        print("0")
    elif A >= 6 and A <= 12:
        print(str(B//2))
    else:
        print(str(B))
