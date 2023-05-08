"""
this python code solves basic linear, quadratic,
equations of higher powers and simulteneous equations
***Uncomment print() to reveal solution***
"""

# importing from Library
from sympy import symbols, solve

# defining the symbols or variables
x,y = symbols("x y")

# solving linear equations
equation = 2*x + 4 - 10
solution = solve(equation,x)
# print('x = ',solution[0])


# solving simulteneous equations
equation_1 = 4*x + 2*y - 10
equation_2 = 2*x + 4*y - 30
solution_1 = solve((equation_1, equation_2), (x,y))
# print(f'x = {(solution_1)[x]}\ny = {solution_1[y]}')


# solving quadratic equations
equation_3 = x**2 -5*x + 6
solution_2 = solve(equation_3, x)
# print(f'x_1 = {solution_2[0]}\nx_2 = {solution_2[1]}')

# solving equations of higher power
equation_4 = x**3 + x**2 + x + 1
solution_3 = solve(equation_4, x)
# print(f'x_1 = {solution_3[0]}\nx_2 = {solution_3[1]}\nx_3 = {solution_3[2]}')





