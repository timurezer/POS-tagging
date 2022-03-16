import sys
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    Doc
)

def read_text(path: str):
    text = None
    with open(path) as f:
        text = f.read()
    return text


def naive_search(arr: list, seq: list):
    """
    Поиск подмассива seq в массиве arr
    """
    positions = []
    n, m = len(arr), len(seq)
    for i in range(n - m + 1):
        if arr[i : i+m] == seq:
            positions.append(i)
    return positions

def pos_search(doc_tokens: list, query: list):
    """
    Поиск последовательности тэгов частей речи query в размеченном тексте (doc_tokens)
    """
    res = []
    m = len(query)
    pos_list = [token.pos for token in doc_tokens]
    positions = naive_search(pos_list, query)
    for i in positions:
        words = [x.text for x in doc_tokens[i:i+m]]
        res.append(words)
    #return res
    for x in res:
        print(' '.join(map(str, x)))

def main():
    segmenter = Segmenter()
    # morph_vocab = MorphVocab()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    text = read_text('text.txt')
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)

    path = sys.argv[1]
    query = sys.argv[2:]
    pos_search(doc.tokens, query)

if __name__ == '__main__':
    main()



