thought=input("whats your to answer to the great question about life,mood,universe?:")
thought=thought.strip().lower()
if thought == "42" or  thought=="forty-two" or thought=="forty two":
    print("yes")
else:
    print("no")
