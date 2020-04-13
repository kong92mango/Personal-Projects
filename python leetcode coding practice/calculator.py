import re

s2 = "1+2+(3+(4+5))"


def calc(s):
    total = 0
    components = re.findall(r"[0-9]+|\+|\-",s)
    print(components)
    op = ""
    for i, v in enumerate(components):
        if i == 0:
            total = int(v)
            continue
        elif v == "+" or v == "-":
            op = v
        else:
            if op == "+":
                total = total + int(v)
            elif op == "-":
                total = total - int(v)
    return(total)


def calc2(s):
    total = 0
    components = re.findall(r"[0-9]+|\+|\-+|\(+|\)",s)
    print(components)
    openIndex = []
    for i, v in enumerate(components):
        if v == "(":
            openIndex.append(i)
        elif v == ")":
            indexStart = openIndex.pop()
            print(components[indexStart:i+1])
            print(components[indexStart+1:i])
            components[indexStart:i+1] = str(calc("".join(components[indexStart+1:i])))
            print(components)
    print(calc("".join(components)))

calc2(s2)
print(eval(s2))
