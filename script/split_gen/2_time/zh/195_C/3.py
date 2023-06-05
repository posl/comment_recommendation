def main():
    a, b, w = map(int, input().split())
    w *= 1000
    ans = [0, 0]
    for i in range(1, w+1):
        if a*i <= w and w <= b*i:
            ans[0] = i
            break
    for i in range(w, 0, -1):
        if a*i <= w and w <= b*i:
            ans[1] = i
            break
    if ans[0] == 0:
        print("UNSATISFIABLE")
    else:
        print(ans[0], ans[1])
