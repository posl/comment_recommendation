def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = [i for i in a if i < p]
    print(len(b))
