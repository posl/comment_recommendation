def main():
    N = int(input())
    T = [int(x) for x in input().split()]
    T.sort()
    print(sum(T)-T[-1]+T[-1]//2)
