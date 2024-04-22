def second_max_n_variables(elements):
    max_v = elements[9]
    for x in elements:
        if x < max_v:
            max_v = x

    second_max_v = elements[8]
    for x in elements:
        if x < second_max_v:
            if x > max_v:
                second_max_v = x 

    return second_max_v

elements = [9, 7, 1, 8]
assert second_max_n_variables(elements) == 8

    