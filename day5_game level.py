import random
while True:
    try:
        level=int(input("level:"))
       
        
    except ValueError:
        pass
    else:
        if level>0:
            break
seceret=random.randint(1,level)
while True:
    try:
        guess=int(input("Guess:"))
    except ValuError:
        continue
    if guess<=0:
        continue
    if guess<seceret:
        print("too small")
    elif guess>seceret:
        print("too large")
    else:
        print("just right")
        break



    
