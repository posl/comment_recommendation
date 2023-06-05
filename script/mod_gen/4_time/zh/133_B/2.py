def get_distance(x, y):
    '''
    计算x和y之间的距离
    '''
    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5

if __name__ == '__main__':
    get_distance()