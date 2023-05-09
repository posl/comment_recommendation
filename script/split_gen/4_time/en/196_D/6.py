def main():
    H, W, A, B = map(int, input().split())
    #print(H, W, A, B)
    #print(H * W, 2 * A + B)
    if H * W == 2 * A + B:
        print("OK")
    else:
        print("NG")
