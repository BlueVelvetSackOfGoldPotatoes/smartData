import pip
import os

def install_each():
    try:
        __import__("pandas")
    except ImportError:
        pip.main(['install', "pandas"])

    try:
        __import__("asyncio")
    except ImportError:
        pip.main(['install', "asyncio"])

    try:
        __import__("nltk")
    except ImportError:
        pip.main(['install', "nltk"])
    # download punctuation related NLTK functions
    # (needed for sent_tokenize())
    nltk.download('punkt')
    # download NLKT part-of-speech tagger
    # (needed for pos_tag())
    nltk.download('averaged_perceptron_tagger')
    # download wordnet
    # (needed for lemmatization)
    nltk.download('wordnet')
    # download stopword lists
    # (needed for stopword removal)
    nltk.download('stopwords')
    # dictionary of English words
    nltk.download('words')

    try:
        __import__("numpy")
    except ImportError:
        pip.main(['install', "numpy"])
        
    try:
        __import__("matplotlib")
    except ImportError:
        pip.main(['install', "matplotlib"])
    
    try:
        __import__("scipy")
    except ImportError:
        pip.main(['install', "scipy"])

    try:
        __import__("sklearn")
    except ImportError:
        pip.main(['install', "sklearn"])

def mass_install():
    os.system("pip install -r requirements.txt")