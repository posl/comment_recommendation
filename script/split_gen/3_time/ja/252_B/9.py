def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #Aの最大値
    max_a = max(A)
    #Bの最小値
    min_b = min(B)
    if max_a > min_b:
        print("Yes")
    else:
        print("No")
