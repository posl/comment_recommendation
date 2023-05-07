def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum_inv = 0
    for a in A:
        sum_inv += 1/a
    print(1/sum_inv)
main()
