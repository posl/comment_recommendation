def main():
    # 1 <= Q <= 2 * 10^5
    # 1 <= P_i <= 3
    # 1 <= X_i <= 10^9
    # All values in input are integers.
    # There is one or more i such that P_i=3.
    # If P_i=3, the bag contains at least one ball just before the i-th operation.
    Q = int(input())
    # 1 <= Q <= 2 * 10^5
    assert 1 <= Q <= 2 * 10**5
    bag = []
    add = 0
    for _ in range(Q):
        query = input().split()
        # 1 <= P_i <= 3
        assert 1 <= int(query[0]) <= 3
        if int(query[0]) == 1:
            # 1 <= X_i <= 10^9
            assert 1 <= int(query[1]) <= 10**9
            bag.append(int(query[1]) - add)
        elif int(query[0]) == 2:
            # 1 <= X_i <= 10^9
            assert 1 <= int(query[1]) <= 10**9
            add += int(query[1])
        else:
            # 1 <= X_i <= 10^9
            assert 1 <= min(bag) <= 10**9
            print(min(bag) + add)
            bag.remove(min(bag))
