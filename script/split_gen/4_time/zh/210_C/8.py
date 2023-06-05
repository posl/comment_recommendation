def main():
    n,k = map(int, input().split())
    c = list(map(int, input().split()))
    count = 0
    for i in range(n-k+1):
        if len(set(c[i:i+k])) > count:
            count = len(set(c[i:i+k]))
    print(count)
