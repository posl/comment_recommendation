def main():
    n = int(input())
    v = list(map(int,input().split()))
    v.sort(reverse=True)
    for i in range(n-1):
        v.append((v.pop()+v.pop())/2)
    print(v[0])

if __name__ == '__main__':
    main()