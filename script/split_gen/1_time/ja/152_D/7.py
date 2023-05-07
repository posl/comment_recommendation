def main():
    N = int(input())
    # 10 進数表記で表したときの桁数を求める
    def digit(n):
        if n == 0:
            return 1
        else:
            return len(str(n))
    # 10 進数表記で表したときの先頭の桁を求める
    def head(n):
        return int(str(n)[0])
    # 10 進数表記で表したときの末尾の桁を求める
    def tail(n):
        return int(str(n)[-1])
    # 10 進数表記で表したときの先頭の桁と末尾の桁が等しいか否かを判定する
    def head_tail(n):
        return head(n) == tail(n)
    # 10 進数表記で表したときの末尾の桁と先頭の桁が等しいか否かを判定する
    def tail_head(n):
        return tail(n) == head(n)
    # 10 進数表記で表したときの先頭の桁と末尾の桁が等しいものの個数を求める
    def head_tail_count(n):
        count = 0
        for i in range(1, n+1):
            if head_tail(i):
                count += 1
        return count
    # 10 進数表記で表したときの末尾の桁と先頭の桁が等しいものの個数を求める
    def tail_head_count(n):
        count = 0
        for i in range(1, n+1):
            if tail_head(i):
                count += 1
        return count
    # 10 進数表記で表したときの先頭の桁と末尾の桁が等しいものの個数を求める
    def head_tail_count2(n):
        count = 0
        for i in range(1, n+1):
            if
