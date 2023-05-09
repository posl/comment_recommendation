def main():
    A,B = map(int,input().split())
    if B < A or B > 6*A:
        print("No")
    else:
        print("Yes")
