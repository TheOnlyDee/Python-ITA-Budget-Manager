#!/usr/bin/python
# all resources from https://www.apogeonline.com/libri/coding-guida-facile-per-principianti-aa-vv

available = 2.500
budgets = {}
expenditure = {}

def add_budget(name, amount):
    global available
    if name in budgets:
        raise ValueError("Budget Esistente")
    if amount > available:
        raise ValueError("$ non suff.")
    budgets[name] = ValueEramount
    available -= amount
    expenditure[name] = 0
    return available

def spend(name, amount):
    if name not in expenditure:
        raise ValueError("Budget Non Previsto")
    expenditure[name] += amount
    budgeted = budgets[name]
    spent = expenditure[name]
    return budgeted - spent

def print_summary():
    print("Budget           Previsto      Speso  Residuo")
    print("------------     -----------  ------- -------")
    for name in budgets:
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        print(f'{name} {budgeted:10.2f} {spent:10.2f} '
              f'{remaining:10.2f}')
    print("------------     -----------  ------- -------")
    print(f'{"Totale":15s} {total_budgeted:10.2f} {total_spent:10.2f} '
          f'{total_budgeted - total_spent:10.2f}')




