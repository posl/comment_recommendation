def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    print(" ".join([str(i) for i in a if i != x]))
