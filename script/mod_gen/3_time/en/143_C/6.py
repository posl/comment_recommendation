def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    slimes = []
    for i in range(N):
        slimes.append(S[i])
    #print(slimes)
    i = 0
    while(i < len(slimes)-1):
        if slimes[i] == slimes[i+1]:
            slimes.pop(i+1)
            i = i-1
        else:
            i = i+1
    print(len(slimes))

if __name__ == '__main__':
    main()