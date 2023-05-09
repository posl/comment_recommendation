def main():
    S = list(input())
    for i in range(1, 10):
        if str(i) in S:
            print("Yes")
            return
    for i in range(1, 10):
        for j in range(1, 10):
            if str(i) in S and str(j) in S:
                if (i*10 + j) % 8 == 0:
                    print("Yes")
                    return
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if str(i) in S and str(j) in S and str(k) in S:
                    if (i*100 + j*10 + k) % 8 == 0:
                        print("Yes")
                        return
    print("No")
    return
