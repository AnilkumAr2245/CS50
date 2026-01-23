def main():
    words=input("camelCase:")
    print(snake_case(words))
def snake_case(words):
    string=("")
    for word in words:
        if word.isupper():
            word=word.lower()
            string+="_"+word
        else:
            string+=word

    return string

main()
