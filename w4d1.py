def count_sheep(sheep_list):
    count = 0
    for sheep in sheep_list:
        if sheep:
            count += 1
    return count