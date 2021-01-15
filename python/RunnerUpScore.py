if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = sorted(list(set(arr)))
    print(a[len(a)-2])
