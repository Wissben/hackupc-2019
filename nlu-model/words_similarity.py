from nltk.corpus import wordnet
import phonetics


def get_synonyms(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())

    return synonyms


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def get_phonetic_transcriptions(word):
    transcriptions = phonetics.dmetaphone(word)
    return transcriptions


def find_phonetic_similarity(name, nameset):
    name_phon = phonetics.soundex(name)
    min = 100
    min_word = ""
    for word in nameset:
        word_phon = phonetics.dmetaphone(word)
        min_edit_distance = levenshtein(word_phon, name_phon)
        if min_edit_distance < min:
            min = min_edit_distance
            min_word = word

    return min_word
