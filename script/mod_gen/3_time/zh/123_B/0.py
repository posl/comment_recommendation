def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    time = [a,b,c,d,e]
    time.sort()
    for i in range(5):
        if time[i] % 10 != 0:
            time[i] = time[i] + 10 - time[i] % 10
    print(time[4])

if __name__ == '__main__':
    main()