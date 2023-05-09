def main():
    a,b,c,d = map(int,input().split())
    if(a*60+b<c*60+d):
        print("Takahashi")
    elif(a*60+b>c*60+d):
        print("Aoki")
    else:
        print("Same")
