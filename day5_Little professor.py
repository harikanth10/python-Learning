import random
while True:
    try:
        level=int(input("level:"))
    except ValueError:
        pass
    else:
        if level in (1,2,3):
            break
score = 0
for _ in range(10):
    if level==1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    
    elif level==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
    else:
        x=random.randint(100,999)
        y=random.randint(100,999)
    tries=0

    while tries < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            answer=None

        if answer == x + y:
            print("Correct")
            score = score + 1
            break
        else:
            print("EEE")
            tries = tries + 1
    if tries == 3:
        print(x + y)
print("Score:", score)
