def main():
    K = int(input())
    H = 21
    M = 0
    if K >= 60:
        H += K // 60
        M = K % 60
    else:
        M = K
    if H >= 24:
        H = H % 24
    if H < 10:
        if M < 10:
            print("0%d:0%d" % (H, M))
        else:
            print("0%d:%d" % (H, M))
    else:
        if M < 10:
            print("%d:0%d" % (H, M))
        else:
            print("%d:%d" % (H, M))
