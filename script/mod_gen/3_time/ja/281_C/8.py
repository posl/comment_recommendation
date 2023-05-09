def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    #print(sum_a)
    t = t % sum_a
    #print(t)
    for i in range(n):
        if t - a[i] < 0:
            print(i+1, t)
            break
        else:
            t = t - a[i]

if __name__ == '__main__':
    main()