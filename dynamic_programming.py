def dynamic_programming(item_count, capacity, items):
    def best_value(i, j):
        if i <= 0 or j <= 0:
            return 0
        weight, value = items[i - 1].weight, items[i - 1].value
        if weight > j:
            return best_value(i - 1, j)
        else:
            return max(best_value(i - 1, j), best_value(i - 1, j - weight) + value)

    j = capacity
    taken = [0] * item_count
    for i in range(item_count, 0, -1):
        if best_value(i, j) != best_value(i - 1, j):
            taken[i - 1] = 1
            j -= items[i - 1].weight
    return best_value(item_count, capacity), taken
