def min_mod(L, R):
    if R-L >= 2019:
        return 0
    else:
        min = 2019
        for i in range(L, R):
            for j in range(i+1, R+1):
                if (i*j)%2019 < min:
                    min = (i*j)%2019
        return min

if __name__ == '__main__':
    min_mod()