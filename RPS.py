from microbit import *

# First attempt using Python - Rock Paper Scissors

display.scroll("Welcome to the Rock Paper Scissors Game - Press A for Rock, B for Paper or A+B for Scissors")

# First, the user inputs R, P or S (A, B, A+B)

if button_a.is_pressed():
    int userChoice = 0
elif button_b.is_pressed():
    int userChoice = 1
elif button_a.is_pressed() and button_b.is_pressed():
    int userChoice = 2

int cpuChoice = random.randint(0, 2)

if userChoice = 0 and cpuChoice = 0:
    display.scroll("The CPU also chose Rock - it's a draw")
elif userChoice = 0 and cpuChoice = 1:
    display.scroll("Oh no, the CPU chose Paper - you lose :(")
elif userChoice = 0 and cpuChoice = 2:
    display.scroll("Wow, you crushed the CPU's scissors - you win!")
elif userChoice = 1 and cpuChoice = 0:
    display.scroll("Nice, you wrapped the CPU's rock with your paper - you win!")
elif userChoice = 1 and cpuChoice = 1:
    display.scroll("You picked the same as the CPU (Paper) - it's a draw")
elif userChoice = 1 and cpuChoice = 2:
    display.scroll("*Snip* - the CPU just cut your paper in half - you lose")
elif userChoice = 2 and cpuChoice = 0:
    display.scroll("You just got CRUSHED by the CPU's rock - you lose")
elif userChoice = 2 and cpuChoice = 1:
    display.scroll("SNIPPER - you just cut the CPU in half - you win!")
elif userChoice = 2 and cpuChoice = 2:
    display.scroll("You both tried to snip each other! - it's a draw")
