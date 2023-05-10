def main():
    K = int(input())
    print("{:02}:{:02}".format((K+2100)//100, (K+2100)%100))
