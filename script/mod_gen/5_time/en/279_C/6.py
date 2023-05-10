def main():
    import sys
    from collections import Counter
    input = sys.stdin.buffer.readline
    H, W = map(int, input().split())
    S = [input().rstrip().decode('utf-8') for _ in range(H)]
    T = [input().rstrip().decode('utf-8') for _ in range(H)]
    S_c = Counter(S)
    T_c = Counter(T)
    if S_c == T_c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()