def main():
    # Read from Standard Input
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    # Solve the problem
    # ...
    # Print the answer to Standard Output
    print("Yes" if solve(h, w, s, t) else "No")

if __name__ == '__main__':
    main()