
# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo: ")
famous_person = input("Pessoa famosa: ")

madlib = f"programar no computador é tão {adj}! isso me deixa feliz porque\
eu amo {verb1}. fique hidratado {verb2} parecido com{famous_person}!"

print(madlib)