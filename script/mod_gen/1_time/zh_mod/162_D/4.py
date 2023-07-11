def main():
    n = int(input())
    s = input()
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            k = 2*j-i
            if k

if __name__ == '__main__':
    main()