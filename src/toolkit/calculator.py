from errors import *
operators = {'+','-','*','/'}
priority_operation = {
    '+': 1,
    '-':1,
    '*':2,
    '/':2
    }
def tokenize(expr:str) -> list[str]:
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
                j+=1
                neg = 0
                while j < len(expr) and expr[j] in '+-':
                    if expr[j] == '-':
                        neg +=1
                    j +=1
                if j < len(expr) and (expr[j].isdigit() or expr[j]=='.'):
                    k = j
                    while k < len(expr) and (expr[k].isdigit() or expr[k] == '.'):
                        k += 1
                    sign = '-' if neg % 2 else '+'
                    tokens.append(sign + expr[j:k])
                    i = k
                    continue
            tokens.append(ch)
            i += 1
            continue
        raise InvalidCharacterError(f"Недопустимый символ:{ch!r}")
    return tokens
def validate(tokens:list[str])->None:
    if not tokens:
        raise EmptyExpressionError("Пустое выражение") 
    prev_op = False
    for pos, el in enumerate(tokens):
        post_op = el in operators
        if post_op:
            if pos == 0 or pos == len(tokens) - 1:
                raise MissingOperandError(f"Пропущен операнд рядом с {el!r}")
            if prev_op == False:
                raise ConsecutiveOperatorsError(f"Два подряд оператора: {el!r}")
        else:
            try:
                float(el)
            except ValueError:
                raise InvalidNumberError(f"Неверное число: {el!r}") from None
def calculate(expr: str) -> list[str]:
    tokens = tokenize(expr)
    validate(expr)
    return solve_rpl(transf_rpl(tokens))
def transf_rpl(expr:list[str]) -> list[str]:
    outstr: list[str] = []
    stack: list[str] = []
    for tok in expr:
        if tok in operators:
            while (stack and stack[-1] in operators
                   and priority_operation[stack[-1]] >= priority_operation[tok]):
                outstr.append(stack.pop())
            stack.append(tok)
        else:
            outstr.append(tok)
    while stack:
        outstr.append(stack.pop())
    return outstr

def solve_rpl(rpn: list[str]) -> float:
    stack: list[str] = []
    for tok in rpn:
        if tok not in operators:
            stack.append(float(tok))
            continue
        right =stack.pop()
        left = stack.pop()
        if tok == '+':
            stack.append(left + right)
        elif tok == '-':
            stack.append(left - right)
        elif tok == '*':
            stack.append(left*right)
        elif tok == '/':
            stack.append(left/right)
        else:
            raise DivisionByZeroError("Деление на ноль")
    return stack[0]