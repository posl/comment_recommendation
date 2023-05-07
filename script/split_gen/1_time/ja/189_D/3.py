def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # y_0 = x_0
    # i >= 1 のとき、S_i が AND なら y_i=y_{i-1} ∧ x_i、S_i が OR なら y_i=y_{i-1} ∨ x_i
    # a ∧ b は a と b の論理積を表し、a ∨ b は a と b の論理和を表します。
    # a と b の論理積は、a と b のどちらかが False なら False で、両方が True なら True です。
    # a と b の論理和は、a と b のどちらかが True なら True で、両方が False なら False です。
    # y_0 = x_0 なので、y_0 は True か False です。
    # y_0 が True のとき、y_1 は x_1 によらず True です。
    # y_0 が False のとき、y_1 は x_1 によらず False です。
    # y_1 が True のとき、y_2 は x_2 によらず True です。
    # y_1 が False のとき、y_2 は x_2 によらず False です。
    # ...
    # y_{N-1} が True のとき、y_N は x_N によらず True です。
    # y_{N-1} が False のとき、y_N は x_N によらず False です。
    # y_N が True のとき、y_N は x_N によらず True です。
    # y_N が False のとき、y_N は x_N によらず False です。
    # つまり、y_i は x_i によらず True または
