def main():
    k = int(input())
    h = k//60
    m = k%60
    print('{:02d}:{:02d}'.format(h+21, m))
