#Roma Razdan
#I plege my honor that I have abided by the Stevens Honor System.

def counter(txt):
    return [len(txt),txt]
from functools import reduce
listOfLists = []
final = []
final2 = []
def longest(y):
    final = list(map(counter,y))
    final2 = (reduce(max,final))
    return final2[1]
