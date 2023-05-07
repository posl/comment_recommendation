def main():
    N = int(input())
    h = list(map(int, input().split()))
    print(N - len(set(h)))
