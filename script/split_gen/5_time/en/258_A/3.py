def main():
    k = int(input())
    print(str(21+(k//60)).zfill(2)+":"+str(k%60).zfill(2))
