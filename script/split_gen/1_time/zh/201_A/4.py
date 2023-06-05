def main():
    #读取输入
    line = input()
    #将输入的字符串分割成3个数字
    A = line.split()
    #将字符串转换成数字
    #map(function, iterable, ...)
    #map() 会根据提供的函数对指定序列做映射。
    #第一个参数 function 以参数序列中的每一个元素调用 function 函数，
    #返回包含每次 function 函数返回值的新列表。
    #map() 函数语法：
    #map(function, iterable, ...)
    #参数
    #function -- 函数
    #iterable -- 一个或多个序列
    #返回值
    #Python 2.x 返回列表。
    #Python 3.x 返回迭代器。
    A = list(map(int, A))
    #判断A的元素能否重新排列成算术序列
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")
