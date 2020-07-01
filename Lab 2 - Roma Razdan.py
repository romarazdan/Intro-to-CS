#Roma Razdan
#I plege my honor that I have abided by the Stevens Honor System.

def dotProduct(L,K):
    if L == [] or K == []:
        return 0
    else:
        return L[0]*K[0]+ dotProduct(L[1:], K[1:])

def expand(S):
    if S == "":
        return []
    else:
        return [S[0]] + expand(S[1:])

def deepMember(e,L):
    if L == []:
        return False
    else:
        if isinstance(L[0], list):
            head,tail = L[0], L[1:]
            return deepMember(e, L[0] or deepMember(e,tail)
        else:
            if e == L[0]:
                return True
            else:
                return deepMemeber(e, L[1:])

def removeAll(e,L):
    if L == [] or L == "":
        return []
    if L[0] == e:
        return removeAll(e,L[1:])
    return [L[0]] + removeAll(e, L[1:])

def even(X):
    if (X % 2 == 0):
        return True
    else:
        return False
def myFilter(x, L):
    if not L:
        return []
    if x([0]) == True:
        return [L(0)] + myFilter(x, L[1:])
    else:
        return myFilter(x, L[1:])
    
def deepReverse(L):
    if L == []:
        return []
    if isinstance(L[-1],list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    return [L[-1]] + deepReverse(L[:-1])
