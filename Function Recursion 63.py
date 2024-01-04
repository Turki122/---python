#------------------
#----Function Recursion ------
#------------------------------------------
#------------------------------------------
#------- To Understand Recursion , You Need To First Understand Recursion -----
#------------------------------------------------------------------------------

# Test Word [wwwoooorrrldd]  x = "wwwoooorrrldd"    print(x[1:])

def cleamword(word) :

    if len(word) == 1 :

        return word

    print(f"print Start Function {word}")

    if word[0] == word[1] : # wwwoooorrrldd

        print(f"print Befo Return {word}")

        return cleamword(word[1:])

    print(f"print Befo Return {word}")

    return word[0] + cleamword(word[1:])
                              # Stash [word]
print(cleamword("wwwoooorrrldd"))
