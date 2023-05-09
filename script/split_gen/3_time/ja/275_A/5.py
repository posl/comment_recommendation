def main():
    N = int(input())
    H = list(map(int, input().split()))
    Hmax = max(H)
    print(H.index(Hmax)+1)
