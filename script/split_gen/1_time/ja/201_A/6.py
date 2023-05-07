def main():
    A = list(map(int, input().split()))
    if len(set(A)) == 2:
        print("Yes")
    else:
        print("No")
