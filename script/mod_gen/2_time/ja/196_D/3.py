def main():
    H, W, A, B = map(int, input().split())
    count = 0
    for i in range(2 ** (H * W)):
        s = bin(i)[2:].zfill(H * W)
        if s.count('1') == A:
            m = [[s[j * W + k] for k in range(W)] for j in range(H)]
            if m == list(map(list, zip(*m))):
                count += 1
    print(count)

if __name__ == '__main__':
    main()