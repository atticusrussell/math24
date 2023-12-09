import itertools
import operator
import sys
from fractions import Fraction

def solve_math24(numbers):
    # Convert numbers to Fractions if not floats
    processed_numbers = []
    for n in numbers:        
        if isinstance(n, str):
            if '.' in n:
                processed_numbers.append(float(n))
            elif '/' in n:
                processed_numbers.append(Fraction(n))
            else:
                processed_numbers.append(int(n))
        elif isinstance(n, float):
            processed_numbers.append(n)
        else:
            # ints can be converted to Fractions over 1
            processed_numbers.append(Fraction(n)) 

    numbers = processed_numbers

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

    # Format numbers based on type (Fraction, float, or int)
    formatted_nums = []
    for num in nums:
        if isinstance(num, float):
            formatted_nums.append(str(num))
        elif isinstance(num, Fraction):
            if num.denominator == 1:
                formatted_nums.append(str(num.numerator))  # Integer representation
            else:
                formatted_nums.append(str(num))  # Fraction representation
        else:
            formatted_nums.append(str(num))

    return pattern.replace('a', formatted_nums[0])\
                  .replace('b', formatted_nums[1])\
                  .replace('c', formatted_nums[2])\
                  .replace('d', formatted_nums[3])\
                  .replace('o', symbols[0], 1)\
                  .replace('o', symbols[1], 1)\
                  .replace('o', symbols[2], 1)

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python3 solve_math24.py num1 num2 num3 num4")
        sys.exit(1)

    # Parse command line arguments
    numbers = sys.argv[1:]

    # Solve and print the solution
    solution = solve_math24(numbers)
    print(f"Solution: {solution}")

if __name__ == "__main__":
    main()
