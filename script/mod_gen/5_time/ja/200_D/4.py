def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        if A[0]%200 == A[1]%200:
            print("Yes")
            print(1,1)
            print(1,2)
            exit()
        else:
            print("No")
            exit()
    else:
        dict = {}
        for i in range(2**N):
            s = str(bin(i)[2:])
            s = s.zfill(N)
            #print(s)
            B = []
            C = []
            for j in range(N):
                if s[j] == "0":
                    B.append(j+1)
                else:
                    C.append(j+1)
            #print(B,C)
            sumB = 0
            sumC = 0
            for b in B:
                sumB += A[b-1]
            for c in C:
                sumC += A[c-1]
            #print(sumB, sumC)
            if sumB%200 == sumC%200:
                if sumB%200 in dict:
                    print("Yes")
                    print(len(dict[sumB%200]), *dict[sumB%200])
                    print(len(B), *B)
                    exit()
                else:
                    dict[sumB%200] = B
        print("No")
        exit()

if __name__ == '__main__':
    main()