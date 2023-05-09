def main():
    # read input
    n, m, x, y = map(int, input().split())
    xa = list(map(int, input().split()))
    ya = list(map(int, input().split()))
    
    # determine war or no war
    if max(xa) >= min(ya) or max(xa) >= y or min(ya) <= x:
        print("War")
    else:
        print("No War")
main()

if __name__ == '__main__':
    main()