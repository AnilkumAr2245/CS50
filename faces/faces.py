def convert(message):
    message=message.replace(":)","🙂")
    message=message.replace(":(","🙁")
    return(message)
def main():
    message=input()
    print(convert(message))
main()


