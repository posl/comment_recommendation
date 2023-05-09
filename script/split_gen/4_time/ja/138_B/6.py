def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_inv = [1/a for a in A]
    A_inv_sum = sum(A_inv)
    print(1/A_inv_sum)
main()  # コード提出時にはコメントアウト
