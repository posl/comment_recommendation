def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    
    if n == 1:
        print(max(a[0], b[0]))
        return
    
    a.sort()
    b.sort()
    a_max = a[-1]
    b_min = b[0]
    if a_max > b_min:
        print(0)
    else:
        print(b_min - a_max + 1)

if __name__ == '__main__':
    main()