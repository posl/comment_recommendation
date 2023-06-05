def main():
    N = int(input())
    for i in range(N):
        d1, d2 = input().split()
        if i >= 2 and d1 == d2 and d0 == d1:
            print("Yes")
            return
        d0 = d1
    print("No")
