def main():
    H = int(input())
    cnt = 0
    while H > 0:
        H = H // 2
        cnt += 1
    print(2 ** cnt - 1)
