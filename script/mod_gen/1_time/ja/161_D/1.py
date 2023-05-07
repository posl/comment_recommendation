def main():
    K = int(input())
    count = 0
    for i in range(1, 10):
        count += 1
        if count == K:
            print(i)
            return
        for j in range(0, 10):
            count += 1
            if count == K:
                print(int(str(i)+str(j)))
                return
            for k in range(0, 10):
                count += 1
                if count == K:
                    print(int(str(i)+str(j)+str(k)))
                    return
                for l in range(0, 10):
                    count += 1
                    if count == K:
                        print(int(str(i)+str(j)+str(k)+str(l)))
                        return
                    for m in range(0, 10):
                        count += 1
                        if count == K:
                            print(int(str(i)+str(j)+str(k)+str(l)+str(m)))
                            return
                        for n in range(0, 10):
                            count += 1
                            if count == K:
                                print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)))
                                return
                            for o in range(0, 10):
                                count += 1
                                if count == K:
                                    print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)))
                                    return
                                for p in range(0, 10):
                                    count += 1
                                    if count == K:
                                        print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)))
                                        return
                                    for q in range(0, 10):
                                        count += 1
                                        if count == K:
                                            print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)))
                                            return
                                        for r in range(0, 10):
                                            count += 1
                                            if count == K:
                                                print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+str(r)))
                                                return
                                            for s in range(0, 10):
                                                count += 1
                                                if count == K:
                                                    print(int(str(i)+str(j)+str

if __name__ == '__main__':
    main()