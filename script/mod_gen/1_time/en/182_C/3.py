def main():
    n = input()
    l = len(n)
    mod3 = [0, 0, 0]
    for i in range(l):
        mod3[int(n[i]) % 3] += 1
    if mod3[0] > 0:
        print(0)
    elif mod3[1] > 1:
        print(1)
    elif mod3[2] > 1:
        print(1)
    elif mod3[1] == 1 and mod3[2] == 1:
        if l > 1:
            print(2)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()