def main():
    N, M = map(int, input().split())
    #print("N, M = ", N, M)
    #print("")
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        #print("a_i, b_i = ", a_i, b_i)
        #print("")
        a.append(a_i)
        b.append(b_i)
    #print("a = ", a)
    #print("b = ", b)
    #print("")
    #print("len(a) = ", len(a))
    #print("len(b) = ", len(b))
    #print("")
    #print("len(set(a)) = ", len(set(a)))
    #print("len(set(b)) = ", len(set(b)))
    #print("")
    #print("len(set(a)) + len(set(b)) = ", len(set(a)) + len(set(b)))
    #print("")
    #print("len(set(a + b)) = ", len(set(a + b)))
    #print("")
    #print("len(set(a + b)) - len(set(a)) - len(set(b)) = ", len(set(a + b)) - len(set(a)) - len(set(b)))
    #print("")
    print(len(set(a + b)) - len(set(a)) - len(set(b)))
main()

if __name__ == '__main__':
    main()