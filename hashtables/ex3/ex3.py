def intersection(arrays):
    """
    YOUR CODE HERE
    """
    d = {}

    for i in arrays:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    results = [info[0] for info in d.items() if info[1] == len(arrays)]
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
