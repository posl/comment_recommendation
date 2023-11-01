def main():
    n = int(input())
    s = input()
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    res = r * g * b
    for i in range(n-2):
        for j in range(i+1,n-1):
            k = 2*j - i
            if k < n:
                if s[i] != s[j] and

if __name__ == '__main__':
    main()