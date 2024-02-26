# Haunted House Adventure

"""
This Python program simulates an adventure in a haunted house where the player must explore the eerie rooms,
encounter spooky events, and unravel the mysteries hidden within. It incorporates various programming concepts and
techniques including for loops, while loops, infinite loops, nested loops, else statements in loops, break statements,
post-test loops, loop and a half, and boolean decisions.
"""

import random

def explore_haunted_house():
    print("Welcome to the Haunted House Adventure!")
    print("You find yourself standing in front of a mysterious old mansion shrouded in darkness.")
    print("Legend has it that the house is haunted by restless spirits and holds untold secrets.")
    print("Do you dare to enter and uncover the truth?")

    # Boolean decision to enter the haunted house
    while True:
        choice = input("Enter the haunted house? (yes/no): ").lower()
        if choice == "yes":
            explore_rooms()
            break
        elif choice == "no":
            print("You decide not to enter the haunted house. Game over.")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def explore_rooms():
    print("You cautiously step into the dark hallway of the haunted house...")
    # Number of rooms to explore
    num_rooms = random.randint(3, 6)
    for room_number in range(1, num_rooms + 1):
        print(f"\nEntering Room {room_number}...")
        # Random chance to encounter a spooky event in each room
        if random.random() < 0.5:
            spooky_event()
        else:
            print("You explore the room but find nothing unusual.")

def spooky_event():
    print("You feel a chill run down your spine as you sense a presence in the room...")
    print("Suddenly, the room is engulfed in darkness and you hear strange whispers.")
    print("You must make a decision to confront the darkness or flee.")

    # Boolean decision to confront the darkness or flee
    while True:
        choice = input("Confront the darkness or flee? (confront/flee): ").lower()
        if choice == "confront":
            print("You gather your courage and face the darkness head-on!")
            break
        elif choice == "flee":
            print("You panic and flee the room in terror.")
            break
        else:
            print("Invalid choice. Please enter 'confront' or 'flee'.")

# Main program entry point
if __name__ == "__main__":
    explore_haunted_house()
