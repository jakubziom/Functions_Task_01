def palindrome_check(word):
    if str(word)==str(word)[::-1]:
        return True
    else:
        return False


print(palindrome_check('potop'))
print(palindrome_check('sedes'))
print(palindrome_check('kajak'))
print('\n')
print(palindrome_check('potopy'))
print(palindrome_check('kajaki'))
