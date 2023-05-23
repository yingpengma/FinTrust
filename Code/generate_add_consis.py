import numpy as np
import copy

def make_add():
    test_list = np.load("earnings_call_3days.npy")
    increase_list = []
    decrease_list = []
    list = []
    for i in test_list:
        if i[1] == '0.0':
            decrease_list.append(i)
        else:
            increase_list.append(i)
    new = copy.deepcopy(decrease_list)
    for i in range(len(decrease_list)):
        length = len(decrease_list[i][3].split('\n'))
        next = i + 1
        if next == len(decrease_list):
            next = 0
        next_length = len(decrease_list[next][3].split('\n'))
        if length + next_length < 512:
            new[i][3] = (decrease_list[i][3] + '\n' + decrease_list[next][3]).lower()
        list.append(new[i])
    print(len(list))
    new = copy.deepcopy(increase_list)
    for i in range(len(increase_list)):
        length = len(increase_list[i][3].split('\n'))
        next = i + 1
        if next == len(increase_list):
            next = 0
        next_length = len(increase_list[next][3].split('\n'))
        if length + next_length < 512:
            new[i][3] = (increase_list[i][3] + '\n' + increase_list[next][3]).lower()
        list.append(new[i])
    print(len(list))
    np.save("add_earnings_call_3days.npy", list)


if __name__ == "__main__":
    make_add()