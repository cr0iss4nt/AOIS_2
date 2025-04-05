import re


def normalize(formula):
    formula = re.sub(r'(!!)+', '', formula)
    formula = re.sub(r'!(\w)', r'(!\1)', formula)
    while formula[0] == '(':
        balance = 1
        for i in range(1,len(formula)):
            if formula[i] == '(':
                balance += 1
            elif formula[i] == ')':
                balance -= 1
        if balance == 0 and formula[i] == ')':
            formula = formula[1:-1]
        else:
            break
    return formula


def is_atomic_formula(formula):
    pattern = "^([A-Za-z])$"
    return bool(re.match(pattern, formula))


def evaluate_formula(formula):
    formula = formula.replace('1', 'True').replace('0', 'False')
    formula = formula.replace('&', ' and ').replace('|', ' or ')
    formula = formula.replace('>', ' <= ')
    formula = formula.replace('~', ' == ')
    formula = formula.replace('!', ' not ')
    result = eval(formula)

    return str(int(result))
