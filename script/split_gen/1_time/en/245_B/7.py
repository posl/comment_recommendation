def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(2001):
        if i not in a:
            print(i)
            return
