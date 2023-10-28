import wiktionaryparser as wkp
# would some sort of dictionary API be better and/or faster?
# https://github.com/n-wissam/wordreference   ?
# https://dictionaryapi.com/
# https://www.wordsapi.com/
# http://developer.wordnik.com/pricing
# https://www.datamuse.com/api/

def get_translations(word, language='fr'):
    """
    Returns a list of all translations in the specified language for a given word (in all parts of speech) from English Wiktionary
    """
    parser = wkp.WiktionaryParser()
    if language == 'fr':
        parser.set_default_language('french')
    elif language == 'en':
        parser.set_default_language('english')
    elif language == 'el':
        parser.set_default_language('greek')
    word = parser.fetch(word)
    translations = []
    for pos in range(len(word[0]['definitions'])):
        definitions = word[0]['definitions'][pos]['text'][1:]
        for definition in definitions:
            translation = ''
            in_brackets = False
            in_parens = False
            for char in definition:
                if char == '[':
                    in_brackets = True
                elif char == ']':
                    in_brackets = False
                elif char == '(':
                    in_parens = True
                elif char == ')':
                    in_parens = False
                elif not in_brackets:
                    if not in_parens:
                        translation += char
            for thing1 in translation.split(','):
                for thing2 in thing1.split(';'):
                    translations.append(thing2.strip())
    return translations

if __name__ == '__main__':
    # print(get_translations('bonjour')[1])
    # print(get_translations('bonjour','en')[1])
    print(get_translations('bon'))