# Rock-Paper-Scissors – Python Implementation  


This repository contains a Python-based implementation of the classic game **Rock-Paper-Scissors**, where users can challenge the computer and track their gameplay statistics.

---

## 🔹 Features
- Clean and intuitive terminal-based interface  
- Real-time win/loss/tie tracking across the game session  
- Case-insensitive input with appropriate input validation  

---

## 🔹 How to Play
1. Upon starting, the program displays instructions and prompts you to choose your move:
   - `rock`
   - `paper`
   - `scissors`
   - *(Any other input is considered invalid)*
2. Enter your move and press **Enter**.
3. The computer randomly generates its move.
4. The program compares both moves and displays the outcome:
   - **You win**
   - **You lose**
   - **It’s a tie**
5. After each round, you will be prompted to continue or quit the game.

---

## 🔹 Gameplay Loop
The game runs continuously, allowing multiple rounds, until the user decides to quit.

---

## 🔹 Future Enhancements
This project serves as a foundation and can be extended further with features such as:
- Difficulty levels with strategic computer decisions
- Persistent storage for tracking scores across sessions
- Two-player mode (human vs. human)

---

## 🔹 Requirements
- Python 3.x

To run the game:
```bash
python rock_paper_scissors.py
