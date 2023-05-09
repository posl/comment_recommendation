def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    while len(a) > 1:
        a.append(a.pop() % a.pop(0))
        a.sort()
    print(a[0])
