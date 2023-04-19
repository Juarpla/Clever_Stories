#Creativity part: adding more to the story and filling in the right one "a" or "an"
print("\nPlease enter the following: \n")
#Start of data requests for text:
adj = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
excl = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
verb4 = input("verb: ")
#filling in the right one "a" or "an"
def article(word):
    if word[0] in "aeiouAEIOU":
        return "an"
    else:
        return "a"
art = article(animal)
#Output of text formed with new entries:
print("\nYour story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very \n{adj.lower()} {animal.lower()} {verb1.lower()} down the hallway. {excl.capitalize()}! I yelled. But all \nI could think to do was to {verb2.lower()} over and over. Miraculously, \nthat caused it to stop, but not before it tried to {verb3.lower()} \nright in front of my family. That {adj.lower()} {animal.lower()} reminded me \nof my childhood, at the same time, how powerful nature can be.")
print(f"After all, I remembered that if you saw {art} {animal.lower()} it was a symbol of \ngood luck, so you have to {verb4.lower()} with it.")