def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    A = defaultdict(int)
    for _ in range(M):
        input()
        for a in map(int, input().split()):
            A[a] += 1
    
    if all(a % 2 == 0 for a in A.values()):
        print('Yes')
    else:
        print('No')
    
    return

if __name__ == '__main__':
    main()