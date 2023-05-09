def main():
    K = int(input())
    print('{:02d}:{:02d}'.format((K+2100)//100, (K+2100)%100))
