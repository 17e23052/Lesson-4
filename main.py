print("What is your first initial?")
initial = input()
print("What is your surname?")
surname = input()
print("What is your age?")
age = int(input())
print("Do you like Marmite? Yes or no")
marmite = input()
likes_marmite = marmite == "yes"
decades = float(age / 10)
print(f"Well hello {initial} {surname}.")
print(f"It is {likes_marmite} that you like Marmite.")
print(f"This is probably because you are {decades} decades old.")