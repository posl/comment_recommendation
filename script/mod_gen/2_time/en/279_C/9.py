def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    H,W = map(int,input().split())
    S = [input().rstrip() for _ in range(H)]
    T = [input().rstrip() for _ in range(H)]
    if Counter(S) == Counter(T):
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    main()