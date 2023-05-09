def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * N
    for i in A:
        count[i-1] += 1
    for i in count:
        print(i)
