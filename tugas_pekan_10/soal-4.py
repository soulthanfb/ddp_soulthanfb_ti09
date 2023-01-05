<<<<<<< HEAD
#konsonan dari string
def delVowel(inp):
    vowel = ['a','i','u','e','o', ' ']
    outp = ""

    for character in inp:
        if character.lower() not in vowel:
            outp += character
    return outp
=======
#konsonan dari string
def delVowel(inp):
    vowel = ['a','i','u','e','o', ' ']
    outp = ""

    for character in inp:
        if character.lower() not in vowel:
            outp += character
    return outp
>>>>>>> 7a3962629709e01c638a5ccc5de7a2655e5d8c24
print(delVowel("Nurul Fikri"))