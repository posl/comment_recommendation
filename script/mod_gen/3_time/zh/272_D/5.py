def get_min_operation_number(N,M):
    #首先计算出每个点到(1,1)的距离，然后按照距离由小到大排序，从小到大依次进行计算，直到所有点都被计算过
    #初始化一个二维数组，用于存放每个点到(1,1)的距离
    distance = [[0 for i in range(N)] for j in range(N)]
    #初始化一个二维数组，用于存放每个点到(1,1)的距离是否被计算过
    distance_calculated = [[False for i in range(N)] for j in range(N)]
    #初始化一个二维数组，用于存放每个点的坐标
    coordinate = [[0 for i in range(N)] for j in range(N)]
    #初始化一个一维数组，用于存放每个点到(1,1)的距离
    distance1 = [0 for i in range(N*N)]
    #初始化一个一维数组，用于存放每个点的坐标
    coordinate1 = [0 for i in range(N*N)]
    #初始化一个二维数组，用于存放每个点的操作步数
    operation_number = [[0 for i in range(N)] for j in range(N)]
    #初始化一个一维数组，用于存放每个点的操作步数
    operation_number1 = [0 for i in range(N*N)]
    #初始化一个一维数组，用于存放每个点的操作步数是否被计算过
    operation_number_calculated = [False for i in range(N*N)]
    #初始化一个一维数组，用于存放每个点的操作步数是否被计算过
    operation_number_calculated1 = [False for i in range(N*N)]
    #初始化一个一维数组，用于存放每个点的操作步数是否被计算过
    operation_number_calculated2 = [False for i in range(N*N)]
    #初始化一个一维数组，用于存放每个点的操作步数是否

if __name__ == '__main__':
    get_min_operation_number()