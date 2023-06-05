def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    flag = False
    for i in range(N):
        if i + 1 not in B:
            flag = True
    if flag:
        print("Yes")
    else:
        print("No")
