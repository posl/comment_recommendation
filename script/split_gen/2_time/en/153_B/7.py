def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= max(A):
        print("Yes")
    else:
        if H % min(A) == 0:
            print("No")
        else:
            print("Yes")
