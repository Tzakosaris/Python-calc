
def eval(dell):
    stack=[]
    dell=dell.split()
    for i in dell:
        if i=="+":
            x=stack.pop()
            y=stack.pop()
            z=x+y
            stack.append(int(z))
            return z
        elif i=="-":
            x=stack.pop()
            y=stack.pop()
            z=y-x
            stack.append(int(z))
            return z
        elif i=="*":
            x=stack.pop()
            y=stack.pop()
            z=x*y
            stack.append(int(z))
            return z
        elif i=="/":    
            x=stack.pop()
            y=stack.pop()
            z=x/y
            stack.append(int(z))
            return z
        else:
            stack.append(int(i))
def trans(expresion):
    expresion=expresion.split()
    output=""
    stack=[]
    for i in expresion:
        if i=="(":
            stack.append(i)
        elif i==")":
            while stack[-1]!="(":
                p=stack.pop()
                output+=p+ ' '
        elif i=="+":
            while len(stack)!=0 and stack[-1]!="(":
                p=stack.pop()
                output+=p+ ' '
            stack.append(i)
        elif i=="-":
            while len(stack)!=0 and stack[-1]!="(":
                p=stack.pop()
                output+=p+ ' '
            stack.append(i)
        elif i=="*":
            while len(stack)!=0 and stack[-1]!="(" and stack[-1]!="+" and stack[-1]!="-":
                p=stack.pop()
                output+=p+ ' '
            stack.append(i)
        elif i=="/":
            while len(stack)!=0 and stack[-1]!="(" and stack[-1]!="+" and stack[-1]!="-":
                p=stack.pop()
                output+=p+ ' '
            stack.append(i)
        else:
            output+=i+ ' '
    while len(stack)!=0:
        p=stack.pop()
        output+=p+ ' '
    return output
    
print(eval(trans("1 + 1")))

