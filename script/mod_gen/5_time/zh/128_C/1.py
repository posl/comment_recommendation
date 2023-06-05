def get_number_of_combinations(N, M, K, S, P):
    """
    N: number of switches
    M: number of light bulbs
    K: list of number of switches connected to each light bulb
    S: list of switches connected to each light bulb
    P: list of remainders for each light bulb
    """
    combinations = 0
    for i in range(2**N):
        # convert i to binary
        i_binary = "{0:b}".format(i)
        # pad the binary string with 0s
        i_binary = i_binary.zfill(N)
        # check if the switch combination satisfies the remainders
        if satisfies_remainders(i_binary, K, S, P):
            combinations += 1
    return combinations

if __name__ == '__main__':
    get_number_of_combinations()