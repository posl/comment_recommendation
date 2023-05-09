def main():
    N = int(input())
    #貯金箱に入っているお金
    box = 0
    #何日目の夜か
    day = 0
    while True:
        day += 1
        box += day
        if box >= N:
            break
    print(day)

if __name__ == '__main__':
    main()