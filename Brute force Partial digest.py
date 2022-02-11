###########################################
# Mohamed Mahmoud Ali            20188043 #
# Tarek Abd Al-Majed idrees      20188062 #
###########################################

def Algorithm_1(X):
    setNumber = []
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            setNumber.append(abs(X[j] - X[i]))
    setNumber.sort()
    print(setNumber)


def Place(L, X):
    if L == []:
        X.sort()
        print(X)
        return
    y = max(L)
    delta1 = [abs(y - i) for i in X]
    if all(i in L for i in delta1):
        for i in delta1:
            L.remove(i)
        X.append(y)
        Place(L, X)
        X.remove(y)
        L.extend(delta1)

    delta2 = [abs(width - y - i) for i in X]
    if all(j in L for j in delta2):
        for i in delta2:
            L.remove(i)
        X.append(width - y)
        Place(L, X)
        X.remove(width - y)
        L.extend(delta2)
    return


def partialDigest(L):
    global width
    width = max(L)
    L.remove(width)
    X = [0, width]
    Place(L, X)


def main():
    # Algoriithm 1
    print("First Run for first Algorithm  : ")
    X = [0, 2, 4, 7, 10]
    Algorithm_1(X)
    print("Second Run for first Algorithm  : ")
    X = [0, 3, 6, 8, 10]
    Algorithm_1(X)

    print("----------------------------------")

    print("First Run for Second Algorithm : ")
    L = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]
    X = []
    width = 0
    print("All possible X for L")
    partialDigest(L)

    print("Second Run for Second Algorithm : ")
    L = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 9, 9, 10, 11, 12, 15]
    X = []
    width = 0
    print("All possible X for L")
    partialDigest(L)
    print("----------------------------------")


if __name__ == "__main__":
    main()
