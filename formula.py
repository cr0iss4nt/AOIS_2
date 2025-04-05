import re


def normalize(formula):
    formula = formula.replace(' ','')
    formula = re.sub(r'(!!)+', '', formula)
    formula = re.sub(r'!(\w)', r'(!\1)', formula)
    while formula.startswith('(') and formula.endswith(')'):
        balance = 0
        for i, char in enumerate(formula):
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance == 0:
                break
        if balance == 0 and i == len(formula) - 1:
            formula = formula[1:-1].strip()
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
