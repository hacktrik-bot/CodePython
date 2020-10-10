
"""
This program recieve an expression and check if the tags 
(), {} and [] are correctly closed.

bracket_checker("{") // return False
bracket_checker("[]") // return True
"""

def bracket_checker(exp):
    brackets = {"(":")", "{":"}", "[":"]"}
    queue = [""]
    for b in exp:
        if b in brackets:
            queue.append(brackets[b])
        elif b in brackets.values() and b != queue.pop():
            return False
    return queue == [""]

print(bracket_checker("{"))