def main():
    n = int(input())
    s = input()
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    ans = r * g * b
    for i in range(n):
        for j in range(i+1,n):
            k = j + (j - i)
            if k >= n:
                continue

if __name__ == '__main__':
    main()