def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(T[-1])
