def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        if p[i] != i + 1:
            count += 1
    if count > 2:
        print("NO")
    else:
        print("YES")
