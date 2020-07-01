from importlib import reload as Rfrsh
import hmmm

#Name: Roma Razdan
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# Fibonacci! You've already done it in Lab 9
# Now however, you are to do hmmmonacci with
# recursion, & you MUST do so for any credit
# The tests are still the same as from Lab 9
# Tests: f(2) = 1 ■■■ f(5) = 5 ■■■ f(9) = 34
RecFibSeq = """ 
00 read r1
01 setn r3 1
02 nop
03 setn r15 42
04 calln r14 7
05 write r2
06 halt
07 jgtzn r1 10
08 setn r2 0
09 jumpr r14
10 nop
11 pushr r1 r15
12 pushr r14 r15
13 addn r1 -1
14 calln r14 7
15 popr r14 r15
16 popr r1 r15 
17 add r4 r2 r3
18 copy r2 r3
19 copy r3 r4
20 nop 
21 jumpr r14

"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = True

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
