def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = 10**9
    for i in [A,B,C,D,E]:
        if i%10 != 0:
            min_time = min(min_time,i%10)
    print(10*(A//10+B//10+C//10+D//10+E//10)+min_time-10)

if __name__ == '__main__':
    main()