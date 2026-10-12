while True:
    try:
        n=int(input("Enter the Number:"))
        if n<=0:
            continue
    except ValueError:
        pass
    else:
        print("the number is:",n)
        break
