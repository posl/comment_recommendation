def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # 1. Find the minimum time required for one person to reach City 6.
    min_time = min(A, B, C, D, E)
    # 2. Find the minimum number of vehicles required for N people to reach City 6.
    min_num = N // min_time
    if N % min_time != 0:
        min_num += 1
    # 3. Output the minimum time required for all of the people to reach City 6.
    print(min_num + 4)

if __name__ == '__main__':
    main()