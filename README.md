🏗️ Tower of Hanoi Solver - Python
This is a Python-based Tower of Hanoi solver that displays rules, computes steps using recursion, and presents them in a structured format.
This Python project implements the Tower of Hanoi puzzle solver. It provides a step-by-step solution for any given number of disks while displaying the movement of disks between rods. The program also reads and displays the game rules from a text file before starting.
It uses recursion to solve the problem and NumPy & Pandas to display and organize the steps in a readable format.

🚀 Features:
✅ Displays Tower of Hanoi rules from an external file before the game starts
✅ Recursively solves the Tower of Hanoi problem for any number of disks
✅ Shows a detailed step-by-step solution in a tabular format
✅ Uses NumPy for disk representation and Pandas for structured display
✅ Asks if you want to play again after solving

🛠 Installation & Running the Game:
1️⃣ Clone the repository.
2️⃣ Navigate to the project folder.
3️⃣ Install dependencies (if not already installed).
    pip install numpy pandas
4️⃣ Run the program.

🎮 How to Play:
1️⃣ The program first displays the rules of the Tower of Hanoi (stored in rules.txt).
2️⃣ Enter the number of disks you want to play with.
3️⃣ The program calculates the step-by-step moves required to solve the puzzle.
4️⃣ After completion, you can choose to play again or exit.

📌 Example Output:

***** Tower of Hanoi Rules *****
(Contents of rules.txt are displayed here...)

Enter the number of disks: 3

***** Initial State *****
Rod 1 (Source): [3 2 1]
Rod 2 (Target): []
Rod 3 (Auxiliary): []

***** Steps to Solve *****
   Move Disk From Rod  Move Disk To Rod
0                      1                      2
1                      1                      3
2                      2                      3
...

***** Final State *****
Rod 1 (Source): []
Rod 2 (Target): [3 2 1]
Rod 3 (Auxiliary): []

Do you want to play again? (y/n)

⚠️ Known Issues:
Ensure rules.txt exists and has content before running the program.
Input validation is not enforced for number of disks—enter positive integers only.

🤝 Contributing:
Want to improve this project? Fork the repo, make changes, and submit a pull request!


👨‍💻 Developed By:
Er. Jatin Joshi ✨
