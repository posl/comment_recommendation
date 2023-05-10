def lunlun(n):
    if n < 10:
        return n
    else:
        keta = len(str(n))
        if keta == 2:
            return n
        elif keta == 3:
            n1 = int(str(n)[0])
            n2 = int(str(n)[1])
            n3 = int(str(n)[2])
            if n2 == 0:
                return n1*10 + n2
            elif abs(n2-n3) <= 1:
                return n
            else:
                return (n1+1)*10 + n1
        elif keta == 4:
            n1 = int(str(n)[0])
            n2 = int(str(n)[1])
            n3 = int(str(n)[2])
            n4 = int(str(n)[3])
            if n2 == 0:
                return n1*100 + n2*10 + n3
            elif abs(n2-n3) <= 1:
                return n
            elif abs(n3-n4) <= 1:
                return (n1+1)*100 + n1*10 + n1
            else:
                return (n1+1)*100 + n1*10 + n1
        elif keta == 5:
            n1 = int(str(n)[0])
            n2 = int(str(n)[1])
            n3 = int(str(n)[2])
            n4 = int(str(n)[3])
            n5 = int(str(n)[4])
            if n2 == 0:
                return n1*1000 + n2*100 + n3*10 + n4
            elif abs(n2-n3) <= 1:
                return n
            elif abs(n3-n4) <= 1:
                return (n1+1)*1000 + n1*100 + n1*10 + n1
            elif abs(n4-n5) <= 1:
                return (n1+1)*1000 + n1*100 + n1*10 + n1
            else:
                return (n1+1)*1000 + n1*100 + n1*10 + n1
        else:
            n1 = int(str(n)[0])
            n2 = int(str(n)[1])
            n3 = int(str(n)[2])

if __name__ == '__main__':
    lunlun()