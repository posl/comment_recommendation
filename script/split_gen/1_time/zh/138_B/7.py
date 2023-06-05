def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [1/i for i in A]
    print(1/sum(A))
