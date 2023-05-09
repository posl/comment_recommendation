def get_input():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    return (n,x,x_list)

if __name__ == '__main__':
    get_input()