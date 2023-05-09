def main():
    # Write code here
    x,y = map(int,input().split())
    if x*4 >= y and x*2 <= y:
        print("Yes")
    else:
        print("No")
