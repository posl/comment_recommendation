def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((B, A))
    jobs.sort()
    time = 0
    for B, A in jobs:
        time += A
        if time > B:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()