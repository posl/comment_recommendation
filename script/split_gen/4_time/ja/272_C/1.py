def main():
    n = int(input())
    a = list(map(int,input().split()))
    odd = []
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) == 0:
        print(-1)
    else:
        print(sum(even) + min(odd) * (len(odd) - 1))
