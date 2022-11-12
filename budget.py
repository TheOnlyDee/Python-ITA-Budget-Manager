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

def add_summary():
    for name in budgets:
        budgeted = budgets[name]
        spent = expenditure[name]
        remaining = budgeted - spent
        print(name, budgeted, spent, remaining)
         

#test = add_budget("Alimenti", 500)
#print(test)