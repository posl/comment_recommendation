def main():
    L, Q = map(int, input().split())
    #Initialize the list with the length of L
    L_list = [L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            #If c = 1, cut the piece at Mark x into two
            L_list.append(x)
            L_list.append(L-x)
            L_list.sort()
        else:
            #If c = 2, choose the piece with Mark x on it and print its length
            for j in range(len(L_list)):
                if L_list[j] >= x:
                    print(L_list[j])
                    break

if __name__ == '__main__':
    main()