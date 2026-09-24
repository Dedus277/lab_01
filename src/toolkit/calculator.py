from errors import *
operators = {'+','-','*','/'}
priority_operation = {
    '+': 1,
    '-':1,
    '*':2,
    '/':2
    }
def tokenize(expr:str):
    tokens = list[str] = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch.isspace():
            i+=1
            continue
        if ch.isdigit or ch == '.':
            j = i
            while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                j+=1
            tokens.append(expr[i:j])
            i = j
        if ch in operators:
            unar = (not tokens) or (tokens[-1] in operators)
            if unar == True and ch in '+-':
                
