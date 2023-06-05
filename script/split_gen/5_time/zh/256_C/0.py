def get_num_list(h1,h2,h3,w1,w2,w3):
    num_list = []
    for i in range(1,31):
        for j in range(1,31):
            for k in range(1,31):
                for l in range(1,31):
                    for m in range(1,31):
                        for n in range(1,31):
                            if i+j+k == h1 and l+m+n == h2 and i+l == w1 and j+m == w2 and k+n == w3 and i+l+m == h3:
                                num_list.append([i,j,k,l,m,n])
    return num_list
