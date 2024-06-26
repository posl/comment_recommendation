def solve():
    # 读入数据
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # 按照题意，玩家不能使用他/她在第（i-K）轮中使用的手。
    # 因此，我们只需要记录前K轮的手势即可。
    # 为了简化编程，我们使用一个长度为K的数组来记录前K轮的手势。
    # 由于我们只需要记录前K轮的手势，因此我们可以使用一个长度为K的滑动窗口来记录前K轮的手势。
    # 为了方便起见，我们使用一个长度为3的数组来记录前K轮的手势。
    # 该数组的第0个元素表示前K轮的手势中，石头的个数；
    # 该数组的第1个元素表示前K轮的手势中，剪刀的个数；
    # 该数组的第2个元素表示前K轮的手势中，布的个数。
    # 例如，如果前K轮的手势是{布、石头、石头、剪刀、布}，则该数组的值为{2、1、2}。
    # 为了简化编程，我们使用一个长度为3的滑动窗口来记录前K轮的手势。
    # 该滑动窗口的第0个元素表示前K轮的手势中，石头的个数；
    # 该滑动窗口的第1个元素表示前K轮的手势中，剪刀的个数；
    # 该滑动窗口的第2个元素表示前K轮的手势中，布的个数。
    # 例如，如果前K轮的手势是{布、石头、石头、剪刀、布}，

if __name__ == '__main__':
    solve()