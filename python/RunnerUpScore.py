if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    champion = runnerup = -100
    for i in arr:
        if i > champion:
            champion = i
        if i >= runnerup and i < champion:
            runnerup = i
    print(runnerup) 
