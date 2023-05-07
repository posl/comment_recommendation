def main():
    A, B = map(int, input().split())
    if A <= 6 and B <= 6:
        if A * 6 >= B:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
