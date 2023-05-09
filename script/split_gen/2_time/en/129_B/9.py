def get_minimum_difference(weights):
    """
    Get the minimum difference between the sum of weights in the first group and the sum of weights in the second group.
    :param weights: List of weights.
    :return: Minimum difference between the sum of weights in the first group and the sum of weights in the second group.
    """
    minimum_difference = float('inf')
    for i in range(1, len(weights)):
        first_group_weights = weights[:i]
        second_group_weights = weights[i:]
        first_group_sum = sum(first_group_weights)
        second_group_sum = sum(second_group_weights)
        difference = abs(first_group_sum - second_group_sum)
        if difference < minimum_difference:
            minimum_difference = difference
    return minimum_difference
