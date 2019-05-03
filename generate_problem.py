import string
import random

def seperate_list(li, number_of_chucks):
    sepators = random.sample(range(0, len(li)), number_of_chucks-1)
    sepators.sort()

    result = []
    current_index = 0
    while len(sepators) != 0:
        current_end = sepators.pop(0)
        result.append(''.join(li[current_index:current_end]))
        current_index = current_end

    result.append(''.join(li[current_index:]))
    return result


def generate_problem(length, number_of_pairs, number_of_letters):
    possible_letters = list(string.ascii_lowercase[:number_of_letters])
    st = random.choices(possible_letters, k=length)
    up = seperate_list(st, number_of_pairs)
    down = seperate_list(st, number_of_pairs)

    result = [(i,j) for i,j in zip(up, down)]
    random.shuffle(result)
    return result


if __name__ == '__main__':
    print(generate_problem(5, 3, 2))

