def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)
