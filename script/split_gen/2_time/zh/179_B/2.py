def main():
    n = int(input())
    count = 0
    for i in range(0, n):
        a, b = map(int, input().split())
        if a == b:
            count += 1
        else:
            count = 0
        if count >= 3:
            break
    if count >= 3:
        print("Yes")
    else:
        print("No")
