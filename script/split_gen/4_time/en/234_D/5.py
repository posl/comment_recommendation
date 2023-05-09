def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n-k):
        if p[i] > p[i+k]:
            print("Yes")
        else:
            print("No")
