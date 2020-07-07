
text_data = ['Test!!!! hello. esim. test2...',
'100% ola!! #HashTag',
'testText???!!?']


def textAnalize(list):
    from unicodedata import category
    AnalizedTexts=[]
    print(list)
    for i in list:
        txt = ""
        for j in i:
            if not category(j).startswith("P") or category(j).startswith("S"):
                print(category(j))
                txt = txt + j
        AnalizedTexts.append(txt)
    return AnalizedTexts

print(textAnalize(text_data))
