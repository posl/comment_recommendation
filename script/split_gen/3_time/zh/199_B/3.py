def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    min_num = max(A)
    max_num = min(B)
    if min_num <= max_num:
        print(max_num - min_num + 1)
    else:
        print(0)
