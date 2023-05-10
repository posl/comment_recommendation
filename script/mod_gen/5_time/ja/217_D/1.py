def main():
    L,Q = map(int,input().split())
    cut = [0,L]
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for j in range(1,len(cut)):
                if cut[j-1] < x and x < cut[j]:
                    print(cut[j] - cut[j-1])
                    break

if __name__ == '__main__':
    main()