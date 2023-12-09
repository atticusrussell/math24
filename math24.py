import itertools
import operator
from fractions import Fraction

def solve_math24(numbers):
    # Convert inputs to fractions to handle decimals and fractions
    numbers = [Fraction(str(n)) for n in numbers]

    # Define operations
    operations = [operator.add, operator.sub, operator.mul, operator.truediv]

    # Generate all permutations of numbers and operations
    for nums in itertools.permutations(numbers):
        for ops in itertools.product(operations, repeat=3):
            # Try different bracket arrangements
            try:
                if ops[0](ops[1](nums[0], nums[1]), ops[2](nums[2], nums[3])) == 24:
                    return format_solution(nums, ops, '((a o b) o c) o d')
                if ops[0](nums[0], ops[1](nums[1], ops[2](nums[2], nums[3]))) == 24:
                    return format_solution(nums, ops, 'a o (b o (c o d))')
                if ops[0](nums[0], ops[1](ops[2](nums[1], nums[2]), nums[3])) == 24:
                    return format_solution(nums, ops, 'a o ((b o c) o d)')
            except ZeroDivisionError:
                continue

    return "No solution possible"

def format_solution(nums, ops, pattern):
    op_symbols = {operator.add: '+', operator.sub: '-', operator.mul: '*', operator.truediv: '/'}
    symbols = [op_symbols[op] for op in ops]
    nums = [str(num) for num in nums]
    return pattern.replace('a', nums[0]).replace('b', nums[1]).replace('c', nums[2]).replace('d', nums[3])\
                  .replace('o', symbols[0], 1).replace('o', symbols[1], 1).replace('o', symbols[2], 1)

# Example usage
print(solve_math24([1.5, 6, 8, 9]))  # Example input
