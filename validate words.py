def main():
    t = open("words.txt","r")
    x = set(y.strip("\n").lower() for y in t.readlines() if y.strip("\n").isalpha())
    t.close()
    file = open("words.txt","w")
    file.write("\n".join(sorted(list(x))))
    file.close()
if __name__ == "__main__":
    main()
