from functools import reduce
import collections
from collections import defaultdict


def increment(iterable):
    result = list(map(lambda x: x+1, iterable))
    print(result)


def product(string_of_numbers):
    result = reduce((lambda x, y: x * y), string_of_numbers)
    print(result)


def reduce_non_alpha(s):
    result = "".join(letter for letter in s if letter.isalpha())
    return result


def change_letters_to_lower(s):
    result = s.lower()
    return result


def read_from_end(s):
    result = s[::-1]
    return result


def check_if_palindrom(s):
    if(reduce_non_alpha(change_letters_to_lower(s))==reduce_non_alpha(change_letters_to_lower(read_from_end(s)))):
        print ("Ten wyraz jest palindromem")
    else:
        print ("Ten wyraz nie jest palindromem")


def delete_punctuation_marks(s):
    import re, string
    out = re.sub('[%s]' % re.escape(string.punctuation), '', s)
    return out


def tokenize(text):
    x = delete_punctuation_marks(text)
    result = change_letters_to_lower(x).split()
    return result


# make read file an array of strings
def read_file(filename):
    with open(filename, encoding='UTF-8') as input_file:
        x = delete_punctuation_marks(input_file.read())
        text = x.split()
        return text


def remove_stopwords(text):
    stopwords = set(read_file("pl.stopwords.txt"))
    text = " ".join(word for word in text.split() if (word not in stopwords and len(word) > 2))
    return text


# read file as string
def read_file_as_string(filename):
    with open(filename, encoding='UTF-8') as input_file:
        x = delete_punctuation_marks(input_file.read())
        return x


def count_most_frequent(filename, n):
    wordcount = {}
    text = read_file_as_string(filename)
    y = remove_stopwords(text)
    x = tokenize(y)
    for word in x:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n):
    print (word + ":", count)


def sort_text_file(filename):
    text = read_file(filename)
    new_text = []
    for word in text:
        new_word = ''.join(sorted(word))
        new_text.append(new_word)
    print(new_text)


def find_longest_words(filename, n):
    text = read_file(filename)
    longest_word = ''
    long_words = []
    for x in range(n):
        for word in text:
            if len(word) > len(longest_word):
                longest_word = word
                long_words.append(word)
                word = ''
    print(long_words)


def ex1():
    print("Zadanie 1:")
    increment([1,2,3,4])


def ex2():
    print("Zadanie 2:")
    product([1, 2, 3, 4, 5])


def ex3():
    print("Zadanie 3:")
    check_if_palindrom("KAja./   K")
    check_if_palindrom("platformy PROGRAMOWANIA")


def ex4():
    print("Zadanie 4:")
    print(tokenize("To be or not to be - that is the question [...]"))


def ex5():
    print("Zadanie 5:")
    print(remove_stopwords("a agata aby blachowiak ach lubie acz bratki aczkolwiek programowanie gdyż xd"))


def ex6():
    print("Zadanie 6:")
    print(count_most_frequent("trurl_pl.txt",20))


def ex7():
    print("Zadanie 7:")
    find_longest_words("unixdict.txt", 20)
    sort_text_file("unixdict.txt")


def main():
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6()
    ex7()


if __name__ == "__main__":
    main()
