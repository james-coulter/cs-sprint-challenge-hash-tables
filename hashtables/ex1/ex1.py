def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    d = {}

    for i in range(len(weights)):
        d[weights[i]] = i
    for i in range(len(weights)):
        difference = limit - weights[i]
        if difference in d:
            return (max(i, d[difference]), min(i, d[difference]))
    return None
