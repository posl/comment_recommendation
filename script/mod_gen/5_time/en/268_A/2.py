def distinct_integers(a,b,c,d,e):
    distinct_list = []
    for i in [a,b,c,d,e]:
        if i not in distinct_list:
            distinct_list.append(i)
    return len(distinct_list)

if __name__ == '__main__':
    distinct_integers()