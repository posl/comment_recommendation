def get_input():
    #input()函数返回的是str类型，所以要转换成int类型
    N = int(input())
    S = input().split()
    #map()函数接收两个参数，一个是函数，一个是Iterable，
    #map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
    S = list(map(int,S))
    return N,S

if __name__ == '__main__':
    get_input()