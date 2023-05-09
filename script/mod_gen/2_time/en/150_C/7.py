def get_smaller_count ( perm ) :
    smaller_count = 0
    for i in range ( len ( perm ) ) :
        for j in range ( i + 1 , len ( perm ) ) :
            if perm [ i ] > perm [ j ] :
                smaller_count += 1
    return smaller_count

if __name__ == '__main__':
    get_smaller_count()