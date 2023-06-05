def main():
    N = input()
    k = len(N)
    N = int(N)
    if k == 1:
        if N % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        listN = list(N)
        listN.sort(reverse=True)
        listN = ''.join(listN)
        listN = int(listN)
        if listN % 3 == 0:
            print(0)
        else:
            for i in range(1,k):
                if i == k-1:
                    print(-1)
                    break
                else:
                    listN = list(listN)
                    listN.pop(i)
                    listN = ''.join(listN)
                    listN = int(listN)
                    if listN % 3 == 0:
                        print(i)
                        break
                    else:
                        continue
main()
