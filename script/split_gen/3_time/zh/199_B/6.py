def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for x in range(1, 1001):
        flag = True
        for i in range(n):
            if x < a[i] or x > b[i]:
                flag = False
                break
        if flag:
            count += 1
    print(count)
