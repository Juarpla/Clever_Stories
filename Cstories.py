print("\nPlease enter the following: \n")
#Start of data requests for text:
adj = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
excl = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
#Output of text formed with new entries:
print("\nYour story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very \n{adj.lower()} {animal.lower()} {verb1.lower()} down the hallway. {excl.capitalize()}! I yelled. But all \nI could think to do was to {verb2.lower()} over and over. Miraculously, \nthat caused it to stop, but not before it tried to {verb3.lower()} \nright in front of my family")