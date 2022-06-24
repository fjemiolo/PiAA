class last_occurrence(object):
    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        return self.occurrences[letter]


def boyer_moore_match(text, pattern):
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  # text index
    j = m - 1  # pattern index
    k = 0
    while i < n:
        k += 1
        if text[i] == pattern[j]:
            if j == 0:
                print(k)
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1 + l)
            j = m - 1
    return -1


def show_match(text, pattern):
    p = boyer_moore_match(text, pattern)
    print('Text:  %s' % text)
    print('Match: %s%s' % ('.'*p, pattern))


text = 'Z PAMIĘTNIKA MŁODEJ LEKARKI'
pattern = 'LEK'
show_match(text, pattern)
