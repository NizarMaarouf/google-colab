from sympy import symbols, Eq, solve
x, y = symbols('x y')
eq1 = Eq(4*x + 3*y - 20)
eq2 = Eq(-5*x + 9*y -26)
solve((eq1,eq2), (x, y))
sol_dict = solve((eq1,eq2), (x, y))
print(f'x = {sol_dict[x]}')
print(f'y = {sol_dict[y]}')
