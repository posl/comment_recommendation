def main():
    N = int(input())
    A = list(map(int, input().split()))
    #Aの最大値と最小値を求める
    A_max = max(A)
    A_min = min(A)
    #Aの最大値と最小値の差を求める
    A_diff = A_max - A_min
    print(A_diff)
