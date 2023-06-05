def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    p.append(0)
    result = 0
    for i in range(1, n+1):
        if p[i-1] == i or p[i+1] == i:
            result += 1
    print(result)
