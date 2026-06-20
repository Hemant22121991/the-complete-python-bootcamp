import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    dummy_text = str1.replace(' ','')
    new_set = set(dummy_text.lower())
    fnl_check = ''.join(sorted(new_set))
    print(new_set)
    print(fnl_check)
    if fnl_check == alphabet:
        return True
    else:
        return False
    
print(ispangram("The quick brown fox jumps over the lazy dog"))