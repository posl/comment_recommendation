def main():
    n, k = map(int, input().split())
    p_list = [list(map(int, input().split())) for _ in range(n)]
    for p in p_list:
        if sum(p) < k*3:
            print("Yes")
        else:
            print("No")
