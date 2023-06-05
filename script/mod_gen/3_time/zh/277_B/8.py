def get_input():
    n = int(input())
    str = []
    for i in range(n):
        str.append(input())
    return n,str

if __name__ == '__main__':
    get_input()