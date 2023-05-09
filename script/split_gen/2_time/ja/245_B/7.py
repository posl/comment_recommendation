def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(set(a))
    a.sort()
    for i in range(n+1):
        if i not in a:
            print(i)
            break
