def main():
    N = int(input())
    A = input().split()
    A = [int(s) for s in A]
    sum = 0
    for i in A:
        sum += 1/i
    print(1/sum)
