prompt=input("enter the camelcase:")
result=""
for c in prompt:
    if c.isupper():
        result=result+"_"+c.lower()
    else:
        result=result+c
print("snakecase:",result)
