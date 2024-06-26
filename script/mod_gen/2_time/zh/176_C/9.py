def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 从后往前遍历，最后一个人的高度是A[-1]，那么他前面的人的高度必须是A[-1]或者A[-1]-1
    # 因为我们要找最小的凳子总高度，所以我们取A[-1]和A[-1]-1中最小的那个
    # 然后往前遍历，每个人的高度必须是他前面的人的高度或者比他前面的人的高度小1
    # 我们每次都取这两个数中较小的那个，直到遍历完所有的人
    # 最后的结果就是我们要找的答案
    # 这里我们使用min()函数来找两个数中较小的那个
    # min()函数的使用方法是min(x, y)，它会返回x和y中较小的那个数
    # 例如min(2, 3)会返回2，min(5, 3)会返回3
    # 这里我们使用min()函数来找两个数中较小的那个
    # min()函数的使用方法是min(x, y)，它会返回x和y中较小的那个数
    # 例如min(2, 3)会返回2，min(5, 3)会返回3
    # 我们从后往前遍历，最后一个人的高度是A[-1]，那么他前面的人的高度必须是A[-1]或者A[-1]-1
    # 因为我们要找最小的凳子总高度，所以我们取A[-1]和A[-1]-1中最小的那个
    # 然后往前遍历，每个人的高度必须是他前面的人的高度或者比他前面的人的

if __name__ == '__main__':
    main()