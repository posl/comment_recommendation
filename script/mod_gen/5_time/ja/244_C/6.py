def main():
    N = int(input())
    a = [0]*(2*N+1)
    for i in range(1,2*N+2):
        a[i-1] = i
    a.sort()
    for i in range(1,2*N+1,2):
        print(a[i],flush=True)
        b = int(input())
        if b == 0:
            break
        else:
            a.remove(b)
            a.remove(i+1)
    else:
        print(a[2*N],flush=True)
        b = int(input())
        if b == 0:
            pass
        else:
            print(a[2*N+1],flush=True)
            b = int(input())
            if b == 0:
                pass
            else:
                print(a[2*N+2],flush=True)
                b = int(input())
                if b == 0:
                    pass
                else:
                    print(a[2*N+3],flush=True)
                    b = int(input())
                    if b == 0:
                        pass
                    else:
                        print(a[2*N+4],flush=True)
                        b = int(input())
                        if b == 0:
                            pass
                        else:
                            print(a[2*N+5],flush=True)
                            b = int(input())
                            if b == 0:
                                pass
                            else:
                                print(a[2*N+6],flush=True)
                                b = int(input())
                                if b == 0:
                                    pass
                                else:
                                    print(a[2*N+7],flush=True)
                                    b = int(input())
                                    if b == 0:
                                        pass
                                    else:
                                        print(a[2*N+8],flush=True)
                                        b = int(input())
                                        if b == 0:
                                            pass
                                        else:
                                            print(a[2*N+9],flush=True)
                                            b = int(input())
                                            if b == 0:
                                                pass
                                            else:
                                                print(a[2*N+10],flush=True)
                                                b = int(input())
                                                if b == 0:
                                                    pass
                                                else:
                                                    print(a[2*N+11],flush=True)
                                                    b = int(input())
                                                    if b == 0:
                                                        pass
                                                    else:
                                                        print(a[2*N+12],flush=True)
                                                        b = int(input())
                                                        if b == 0:
                                                            pass

if __name__ == '__main__':
    main()