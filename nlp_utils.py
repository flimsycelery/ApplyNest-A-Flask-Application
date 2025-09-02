import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = set()

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and token.is_alpha:
            keywords.add(token.lemma_.lower())

    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "TECHNOLOGY", "SKILL"]:
            keywords.add(ent.text.lower())

    return sorted([kw for kw in keywords if len(kw) > 2])
