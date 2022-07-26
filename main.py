from functools import reduce
from sympy import isprime


def job(lsts):
    even_lsts = filter(lambda x: len(x) % 2 == 0, lsts)
    combine = lambda l1, l2: l1 + l2
    super_even_lst = reduce(combine, even_lsts)
    super_even_lst_indecies = list(range(len(super_even_lst) - 1))

    def sababa_index(i):
        return isprime(super_even_lst[i]) and isprime(super_even_lst[i + 1]) and super_even_lst[i + 1] > super_even_lst[i]
    sababa_indecies = list(filter(sababa_index, super_even_lst_indecies))
    return len(sababa_indecies) == len(super_even_lst) - 1


inp1 = [[6, 2, 4], [3, 5], [10], [7, 11, 13, 19]]
o1 = job(inp1)
print(o1)
inp2 = [[6, 2, 4], [3, 11], [], [7, 11, 13, 19]]
o2 = job(inp2)
print(o2)
