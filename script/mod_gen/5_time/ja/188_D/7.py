def get_input_data():
    n,c = map(int,input().split())
    service = []
    for i in range(n):
        a,b,c = map(int,input().split())
        service.append([a,b,c])
    return n,c,service

if __name__ == '__main__':
    get_input_data()