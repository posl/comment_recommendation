def main():
    N = int(input())
    H = list(map(int,input().split()))
    H_max = max(H)
    print(H.index(H_max)+1)
