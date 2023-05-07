def main():
    N = int(input())
    zoro = 0
    for _ in range(N):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            zoro += 1
            if zoro == 3:
                print("Yes")
                return
        else:
            zoro = 0
    print("No")
