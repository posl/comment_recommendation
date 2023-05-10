def main():
    n,k = map(int, input().split())
    c = list(map(int, input().split()))
    #print(n,k,c)
    count = 0
    for i in range(n-k+1):
        count = max(len(set(c[i:i+k])), count)
    print(count)
main()

if __name__ == '__main__':
    main()