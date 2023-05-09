def main():
    n = int(input())
    a = list(map(int, input().split()))
    odd = [i for i in a if i % 2 == 1]
    if len(odd) == 0:
        print(-1)
    else:
        print(sum(a) - sum(odd))
