import re


def normalize(formula):
    formula = re.sub(r'(!!)+', '', formula)
    formula = re.sub(r'!(\w)', r'(!\1)', formula)
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
