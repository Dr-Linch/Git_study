some_text = "Hi guis, my name is Linch"


def text_revers(text: str):
    text_list = []

    for letter in text:
        text_list.append(letter)

    text_list.reverse()
    return ''.join(text_list)


print(text_revers(some_text))
