def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []
    for i in a:
        d[i] = 1
    for i in a:
        if (i * -1) in d and i > 0:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
