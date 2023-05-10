def main():
    n = int(input())
    p = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if i == p[i]:
            result += 1
    if result == n:
        print(n)
        return
    for i in range(n):
        if i == p[i]:
            if i == n-1:
                if p[0] == 0:
                    result += 1
            else:
                if p[i+1] == 0:
                    result += 1
    print(result)
