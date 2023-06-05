def problems252_b():
    n = input()
    a = map(int, raw_input().split())
    k = input()
    b = map(int, raw_input().split())
    max_a = max(a)
    for i in b:
        if a[i-1] == max_a:
            print "Yes"
            return
    print "No"

if __name__ == '__main__':
    problems252_b()