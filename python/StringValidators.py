if __name__ == '__main__':
    s = input()
    
    methods = [
        ["isalnum", False],
        ["isalpha", False],
        ["isdigit", False],
        ["islower", False],
        ["isupper", False]
    ]
   
    for i in range(0,len(s)):
        for method in methods:
            if method[1] is False:
                if eval("s[" + str(i) + "]." + method[0] + "()"):
                    method[1] = True
    
    for method in methods:
        print(method[1])
