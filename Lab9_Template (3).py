# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name: Roma Razdan
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
# Purpose: to implement the learning done in class
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1
01 read r2
02 sub r3 r2 r1
03 sub r4 r1 r2
04 jgtzn r3 06
05 jgtzn r4 08
06 write r2
07 halt
08 write r1
09 halt

"""

# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 ≥ 0
Power = """
00 read r1
01 read r2
02 setn r3 1
03 jeqzn r2 7
04 mul r3 r1 r3
05 addn r2 -1
06 jumpn 3
07 write r3
08 halt

"""

# Fibonacci
#  Write a hmmm function that gets one numner,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 ≥ 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 jeqzn r1 10
02 setn r2 10
03 setn r3 1
04 add r4 r3 r2
05 copy r2 r3
06 copy r3 r4
07 addn r1 -1
08 jgtzn r1 04
09 nop
10 write r2
11 halt 

"""

# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Max  # Change to the function you want to run
doDebug = True # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


