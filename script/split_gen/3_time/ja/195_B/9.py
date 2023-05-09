def main():
    A,B,W = map(int,input().split())
    W = W * 1000
    ans_min = W // B
    ans_max = W // A
    if ans_min * B > W:
        ans_min = ans_min + 1
    if ans_max * A < W:
        ans_max = ans_max - 1
    if ans_min > ans_max:
        print("UNSATISFIABLE")
    else:
        print(ans_min,ans_max)
