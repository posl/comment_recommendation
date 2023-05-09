def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    # 1. 360度をNで割った余りが答え
    # 2. 360度をNで割った余りが0の場合は、答えは360度
    # 3. 360度をNで割った余りが0以外の場合は、答えは360度から余りを引いたもの
    ans = 360 % N
    if ans == 0:
        ans = 360
    else:
        ans = 360 - ans
    print(ans)
