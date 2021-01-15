def swap_case(s):
    final = []
    for i in list(s):
        if(i.isupper()):
            final.append(i.lower())
        else: 
            final.append(i.upper())
    return "".join(final)
