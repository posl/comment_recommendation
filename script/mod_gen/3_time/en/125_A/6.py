def main():
    line = input()
    a,b,t = line.split()
    a = int(a)
    b = int(b)
    t = int(t)
    count = 0
    for i in range(1, t+1):
        if i % a == 0:
            count += b
    print(count)

if __name__ == '__main__':
    main()