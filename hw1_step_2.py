def check_word(new_dict,new):
    for i in new:
        if i in new_dict:
            new_dict[i] -= 1
            if new_dict[i] < 0:
                return False
        if i not in new_dict:
            return False
    return True


def main():
    test = "moonstarer"

    f = open('/usr/share/dict/words')
    lines2 = f.readlines()
    f.close()

    ans = ""

    given = test.lower()
    given_dict = {}

    for i in given:
        if i not in given_dict:
            given_dict[i] = 1
        else:
            given_dict[i] += 1

    for words in lines2:
        new_words = words.lower().strip()
        new_dict = dict(given_dict)
        if check_word(new_dict,new_words):
            if len(ans) < len(new_words):
                ans = words
    print ans

if __name__ == '__main__':
    main()
