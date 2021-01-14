if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = []
    for i in integer_list:
        t.append(i)
        
    print(hash(tuple(t)))
