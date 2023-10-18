def main(n):
    n=round(n)
    if n<=0:
        raise Exception("Number can't be lower than 1")
    result = []
    a = [True] * (n + 1)
    a[0], a[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if a[i]:
            for j in range(2 * i, n + 1, i):
                a[j] = False
    for i in range(2, n):
        if a[i]:
            print(i)
            result.append(i)
    return result