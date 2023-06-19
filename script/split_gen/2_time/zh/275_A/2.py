def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    print(H.index(max(H))+1)
