import sys

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[len(self.items) - 1]
    def push(self,item):
        self.items.append(item)
    def size(self):
        return len(self.items)

# constant
DIGIT = "0123456789"
ADDMINUS = "+-"
ERROR = "Oops!  That was no valid expression.  Try again..."
OPERATOR = "+-*/"
BRACKET = "()"
PRIORITY = {"(":0,"+":1,"-":1,"*":2,"/":2,")":2}  # priority of operator from low to high

# convert from infix expression to postfix expression
def infix_to_postfix(token):
    n = len(token)
    P = Stack()
    Q = Stack()
    for i in range(n):
        if (str(token[i]) == "("): P.push(token[i])
        else:
            if (str(token[i]) == ")"): 
                while True:
                    x = P.pop()
                    if (x != '('):
                        Q.push(x)
                    else: break
                        
            else: 
                if (str(token[i]) in OPERATOR):
                    while P.isEmpty() is not True and PRIORITY[str(token[i])] <= PRIORITY[str(P.top())]:
                        Q.push(str(P.pop()))
                    P.push(token[i])
                else: Q.push(str(token[i]))
                                 
    while not P.isEmpty():
        Q.push(P.pop())
    return Q

# simplify the continuous + and -.  For ex: 1+-2=1+2, 1--2=1+2
def handle_continuous_plus_and_minus(s):
    i = 0
    t = ""
    while i < len(s):
        if (s[i] == '+' or s[i] == '-'):
            j = i + 1
            minus = 0
            if (s[i] == '-'): minus = 1
            while (j < len(s) and s[j] in ADDMINUS):
                if (s[j] == '-'): minus+=1
                j+=1
            i = j
            if (minus % 2 == 1): t = t + '-'
            else: t = t + '+'
        else:
            t = t + s[i]
            i+=1
    return t

# check bracket condition
def check_bracket(s):
    check = True
    # in case a*-b, a*+b, a/-b, a/+b
    for i in range(1,len(s)):
        if (s[i] == '-' or s[i] == '+') and (s[i - 1] == '*' or s[i - 1] == '/'):
            check = False
    # in case number of ( differ from number of )
    if (s.count(')') != s.count('(')):
            check = False

    return check

# handle negative operands by adding 0 before them.  For ex: -3-1=0-3-1
def handle_negetive_operand(s):
    if (s[0] == '+' or s[0] == '-'): s = "0" + s
    i = 1
    while (i < len(s)):
      if (s[i] == '+' or s[i] == '-'):
          if (s[i - 1] == ')'):
             i+=1
             continue
          if (s[i - 1] not in DIGIT):
            s = s[:i] + '0' + s[i:]
            i+=1
          else: i+=1
      else: i+=1
    return s

# split expression into token
def split_expression_into_token(s):
    i = 0
    n = len(s)
    token = []
    while i < n:
        if (s[i] in OPERATOR) or (s[i] in BRACKET):
            token.append(s[i])
            i+=1
        else:
            tmp = str(s[i])
            j = i + 1
            while j < n and s[j] not in OPERATOR and s[j] not in BRACKET:
                tmp = tmp + s[j]
                j+=1
            token.append(tmp)
            i = j 
    return token

# validate expression
def validate_expression(token):
    ok = True
    n=len(token)
    for i in range(n):
        if (token[i] in OPERATOR) or (token[i] in BRACKET): continue
        try:
            value = float(token[i])
            token[i] = str(value)
        except ValueError:
            ok = False            
    return ok

# calculate the value of expression
def calculate_expression(s):

    if (check_bracket(s)==False): return None
    s=handle_continuous_plus_and_minus(s)
    s=handle_negetive_operand(s)
    token=[]
    token=split_expression_into_token(s)
    if (validate_expression(token) == False): return None
    Q=Stack()
    Q=infix_to_postfix(token)
    i = 0
    P = Stack()
    try:
        for i in Q.items:
            if (str(i) in OPERATOR):
                if i == "+":
                    value = P.pop() + P.pop()
                    P.push(value)

                if i == "-":
                    value = -P.pop() + P.pop()
                    P.push(value)                        

                if i == "*":
                    value = P.pop() * P.pop()
                    P.push(value)

                if i == "/":
                    u = P.pop()
                    v = P.pop()
                    try:
                        P.push(v / u)
                    except ZeroDivisionError:
                        print("Error ! ZeroDivisionError")
                        return None
            else:
                P.push(float(i))
        return(P.pop())
    except Exception:
        return None


s=str(input())
value=calculate_expression(s)
if (value!=None): print(value)
else: print(ERROR)

