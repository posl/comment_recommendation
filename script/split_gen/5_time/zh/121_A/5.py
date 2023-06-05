def main():
    h,w = map(int,input().split())
    h1,w1 = map(int,input().split())
    print(h*w-h1*w-w1*h+h1*w1)
