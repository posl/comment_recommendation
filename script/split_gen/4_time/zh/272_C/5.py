def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    max_a = max(a)
    for i in range(max_a+1):
        if i%2==0 and i//2 in a:
            print(i)
            return
    print(-1)
