def main():
    n = int(input())
    count = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            count += 1
            if count >= 3:
                print("Yes")
                return
        else:
            count = 0
    print("No")
