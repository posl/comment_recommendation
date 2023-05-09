def main():
    sheep, wolves = map(int, input().split())
    if wolves >= sheep:
        print('unsafe')
    else:
        print('safe')
