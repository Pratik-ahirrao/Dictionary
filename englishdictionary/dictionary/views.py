from django.shortcuts import render
from PyDictionary import PyDictionary
from englisttohindi.englisttohindi import EngtoHindi
import pyttsx

# Create your views here.


def index(req):
    return render(req, "index.html")


def word(req):
    my_word = req.GET.get('search')  # gets our word
    dictionary = PyDictionary()
    meaning = dictionary.meaning(my_word)
    synonym = dictionary.synonym(my_word)
    antonym = dictionary.antonym(my_word)
    translate = EngtoHindi(my_word).convert
    context = {
        'meaning': meaning['Noun'][0],
        'synonym': synonym,
        'antonym': antonym,
        'translate_toHindi': translate,
    }
    print(synonym)
    return render(req, "word.html", context)
