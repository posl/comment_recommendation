def main():
    x,y = map(float, input().split('.'))
    if y <= 2:
        print('%d-'%x)
    elif y <= 6:
        print('%d'%x)
    else:
        print('%d+'%x)
