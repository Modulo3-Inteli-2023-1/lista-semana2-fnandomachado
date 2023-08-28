def is_anagram(a, b):
    if sorted(a) == sorted(b):
        print(True)
        return True
    else:
        print(False)
        return False
