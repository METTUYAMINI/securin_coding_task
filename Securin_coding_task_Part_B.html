def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result

def get_dice_sums(dice):
    sums = [sum(combination) for combination in product(*dice)]
    return sums

def generate_all_configurations(max_value, length):
    return list(product(range(1, max_value + 1), repeat=length))

def undoom_dice(Die_A, Die_B):
    # Calculate original probabilities
    original_sums = get_dice_sums([Die_A, Die_B])
    unique_sums = set(original_sums)
    original_probabilities = {sum_val: original_sums.count(sum_val) / len(original_sums) for sum_val in unique_sums}

    # Generate all possible configurations for Die_A with no more than 4 spots
    possible_configs_A = generate_all_configurations(4, len(Die_A))

    # Filter configurations based on the original probabilities
    valid_configs_A = [
        config for config in possible_configs_A
        if all(x <= 4 for x in config) and get_dice_sums([config, Die_B]) == original_sums
    ]

    if not valid_configs_A:
        return Die_A, Die_B

    new_die_A = valid_configs_A[0]

    return new_die_A, Die_B