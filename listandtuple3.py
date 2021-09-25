import sys

horsemen = ['war', 'famine', 'pestilence', 'death']
membership = 'pestilence' in horsemen
print(membership)
#sys.exit(0)
membership = 'apocolypse' in horsemen
print(membership)
print()
#sys.exit(0)

for horsemen in horsemen:
    print(horsemen, "\t", end=" ")
print()
#sys.exit(0)
print()
for fruit in ["banana", "apple", "quince"]:
    print("I like to eat " + fruit + "s!")