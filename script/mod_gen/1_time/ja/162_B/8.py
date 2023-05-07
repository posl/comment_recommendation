def main():
    N = int(input())
    print(sum([i if i%3!=0 and i%5!=0 else 0 for i in range(1,N+1)]) + 3*sum([i if i%3==0 and i%5!=0 else 0 for i in range(1,N+1)]) + 5*sum([i if i%3!=0 and i%5==0 else 0 for i in range(1,N+1)]))

if __name__ == '__main__':
    main()