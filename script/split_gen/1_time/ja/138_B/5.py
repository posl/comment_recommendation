def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1/sum(1/x for x in A))
