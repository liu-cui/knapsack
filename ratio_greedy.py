def ratio_greedy(item_count, capacity, items):
    ratios = [(index, float(item.value) / float(item.weight)) for index, item in enumerate(items)]
    ratios = sorted(ratios, key=lambda x: x[1], reverse=True)
    value = 0
    weight = 0
    taken = [0] * item_count

    for index, ratio in ratios:
        if items[index].weight + weight <= capacity:
            weight += items[index].weight
            value += items[index].value
            taken[index] = 1
    return value, taken
