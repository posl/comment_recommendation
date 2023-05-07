def main():
    #入力
    A, B = map(int, input().split())
    #出力
    for i in range(1,1000):
        if i*0.08 == int(i*0.08) and i*0.1 == int(i*0.1):
            if int(i*0.08) == A and int(i*0.1) == B:
                print(i)
                exit()
    print(-1)
