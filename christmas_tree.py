
def main(x):
    # x is the tree high (trunk excluded)
    albero = [f"{('*'*n):>{x-1}}" + "*" + f"{('*'*n):<{x-1}}" for n in (*range(x), 0, 0)]
    print("\n".join(albero))

if __name__ == "__main__":
    main(5)
