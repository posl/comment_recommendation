def jump(n, x, ab):
    #print(n, x, ab)
    for i in range(n):
        if x >= ab[i][0] and x <= ab[i][1]:
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    jump()