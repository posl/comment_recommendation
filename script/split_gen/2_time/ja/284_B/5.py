def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(len([i for i in A if i % 2 == 1]))
