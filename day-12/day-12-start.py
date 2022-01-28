################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
#   new variables/functions created are accessible only within the function

def drink_potion():
    potion_str = 2
    print(potion_str)

drink_potion()
#print(potion_str)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_str = 2
        print(player_health)
    drink_potion()

print(player_health)