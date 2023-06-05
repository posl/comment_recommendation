def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_num = min(a,b,c,d,e)
    time = n // min_num
    if n % min_num != 0:
        time += 1
    print(time+4)

if __name__ == '__main__':
    main()