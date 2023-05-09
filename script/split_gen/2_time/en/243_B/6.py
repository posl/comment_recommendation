def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                count += 1
                break
    print(count)
    print(count - n)
