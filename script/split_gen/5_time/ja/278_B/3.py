def main():
    H, M = map(int, input().split())
    if M < 30:
        if H == 0:
            print(23, M+30)
        else:
            print(H-1, M+30)
    else:
        print(H, M-30)
