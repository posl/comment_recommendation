def jump(jumps, x):
    if jumps[0][1] >= x:
        return 'Yes'
    for i in range(1, len(jumps)):
        if jumps[i][0] >= jumps[i-1][1] and jumps[i][1] >= x:
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    jump()