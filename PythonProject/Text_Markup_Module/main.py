##Sumy-1
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.text_rank import TextRankSummarizer
# #import nltk
# #nltk.download('punkt_tab')
#
# FILE_PATH = 'example'
#
# parser = PlaintextParser.from_file(FILE_PATH, Tokenizer("russian"))
# summarizer = TextRankSummarizer()
#
# # Допустим, хотим получить 50 предложений.
# summary = summarizer(parser.document, 50)
#
# i = 1
#
# for sentence in summary:
#     print(i, " .", sentence)
#     i+=1

# #PyTextRank - 2
# import spacy
# import pytextrank
#
# # Загружаем русскоязычную модель spaCy
# nlp = spacy.load('ru_core_news_md')
#
# # Подключаем PyTextRank к пайплайну spaCy
# nlp.add_pipe("textrank", last=True)
#
# with open('example', 'r', encoding='utf-8') as f:
#     text = f.read()
#
# doc = nlp(text)
#
# i=1
# # Итеративно получаем предложения (chunks), ранжированные по важности
# for sent in doc._.textrank.summary(limit_phrases=10, limit_sentences=100):
#     print(i, ".", sent)
#     i+=1
