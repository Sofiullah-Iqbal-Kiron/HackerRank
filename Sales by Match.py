# accepted in first attempt
# Time Complexity: O(n)


def sockMerchant(n, ar):
    socksCounter = [0] * 101
    pairs = 0

    for number in ar:
        socksCounter[number] += 1

        if socksCounter[number] != 0 and socksCounter[number] % 2 == 0:
            pairs += 1

    return pairs
