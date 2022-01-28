################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope
#   new variables/functions created are accessible only within the function

# def drink_potion():
#     potion_str = 2
#     print(potion_str)

# drink_potion()
#print(potion_str)

# Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_str = 2
#         print(player_health)
#     drink_potion()

# print(player_health)

# There is no Block Scope

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

# Modifying Global Scope

# enemies = 1

# def increase_enemies():
#     # global enemies
#     # to make variable accessible in a function
#     # enemies += 1
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants
# Use upper case to realise that not to change variables
PI = 3.14159