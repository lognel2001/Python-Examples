game_list = ("Werewolf: surive the night",
             "Clash Royale",
             "Super Smash Bros wii",
             "Pokemon Leaf Green",
             "Pokemon Soul Silver",
             "Lego Starwars",
             "Age of Mythology the titans",
             "007 N64",
             "New Super Mario Bros wii",
             "Pokemon Stadium")
print(len(game_list))
num5game=game_list[4]
print(num5game)
middle5 = game_list[3:7]
print(middle5)
last4 = game_list[6:]
print(last4)
evens = game_list[::2]
print(evens)
backward= game_list[::-1]
print(backward)
for i in game_list:
    print(i)
print(game_list)
game_list +=("11",12,12.0,14,"15")
print(game_list)
game_list[0]="WOW"
game_list[1] = "zelda link to the past"
print(game_list)
