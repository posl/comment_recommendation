def main():
    #read input
    R = int(input())
    #print(R)
    
    #process
    if R < 1200:
        print("ABC")
    elif R < 2800:
        print("ARC")
    else:
        print("AGC")
