def main():
    n, k = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, x[i+k-1] - x[i] + min(abs(x[i+k-1]), abs(x[i])))
    
    print(ans)
main()
This is a Python 3 solution.
The algorithm is as follows:
Sort the candles in ascending order.
Check the minimum time for each case where the starting point is in the range of the first candle to the last candle.
The minimum time is the minimum time of the following two:
The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.
The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.
The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.
The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.
The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.
The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.
The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.
The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.
The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.
The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.
The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.
The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.
The time required to move from the starting point to the rightmost candle, and then to the leftmost candle.
The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.
The time required to move from the starting point to the leftmost candle, and then to the rightmost candle.
The time required to move from the starting point to the

if __name__ == '__main__':
    main()