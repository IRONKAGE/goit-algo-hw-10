import pulp

model = pulp.LpProblem("Maximize_Beverage_Production", pulp.LpMaximize)
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total_Production"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"         # Вода
model += 1 * lemonade <= 50, "Sugar_Constraint"                            # Цукор
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"                      # Лимонний сік
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"                   # Фруктове пюре

model.solve()

# Приклад використання:
print(f"Статус рішення: {pulp.LpStatus[model.status]}")
print(f"Виробити Лимонаду: {int(pulp.value(lemonade))} од.")
print(f"Виробити Фруктового соку: {int(pulp.value(fruit_juice))} од.")
print(f"Загальна кількість продуктів: {int(pulp.value(model.objective))} од.")
