# given a sortable list, create a functional sort algorithm
def fqsort(x):
    if len(x) > 1:
        return [*fqsort(list(filter(lambda y: y < x[0], x))),
                *list(filter(lambda y: y == x[0], x)),
                *fqsort(list(filter(lambda y: y > x[0], x)))]
    else:
        return x
