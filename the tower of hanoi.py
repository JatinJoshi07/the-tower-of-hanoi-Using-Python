import numpy as np
import pandas as pd
import os

file_path = r" " #add path of rules.txt

def display_rules(file_path):
    with open(file_path, 'r') as file:
        rules = file.read()
    print("***** Tower of Hanoi Rules *****")
    print(rules)
    print()

def solve(n, source, target, auxiliary, steps):
    if n == 1:
        steps.append((source, target))
        return
    solve(n - 1, source, auxiliary, target, steps)
    steps.append((source, target))
    solve(n - 1, auxiliary, target, source, steps)

def display_steps(steps):
    df = pd.DataFrame(steps, columns=["Move Disk From Rod", "Move Disk To Rod"])
    print("\n***** Steps to Solve *****")
    print(df)

def play_again():
    print()
    print("Do you want to play again? (y/n)")
    PA = input().strip().lower()
    if PA == 'y':
        T_O_H()
    elif PA == 'n':
        print("Thank you for playing! Have a great day!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        play_again()

def T_O_H():
    display_rules(file_path)
    num_Disk = int(input("Enter the number of disks: "))
    source = np.arange(num_Disk, 0, -1)
    target = np.array([], dtype=int)
    auxiliary = np.array([], dtype=int)
    print("\n***** Initial State *****")
    print(f"Rod 1 (Source): {source}")
    print(f"Rod 2 (Target): {target}")
    print(f"Rod 3 (Auxiliary): {auxiliary}")
    steps = []
    solve(num_Disk, "1", "2", "3", steps)
    display_steps(steps)
    print("\n***** Final State *****")
    print(f"Rod 1 (Source): {[]}")
    print(f"Rod 2 (Target): {np.arange(num_Disk, 0, -1)}")
    print(f"Rod 3 (Auxiliary): {[]}")
    play_again()

if __name__ == "__main__":
    T_O_H()
