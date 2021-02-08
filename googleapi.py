"""A scrpt to query the api of googlebooks and parse the results as information to be stored in a database"""

import requests
import json
from dataclasses import dataclass, asdict


def book_info(booknumber:str, title_str: str, author_str: str)-> dict:
    """Function queries the google API and returns book data for a particular ISBN"""
    base_url =  "https://www.googleapis.com/books/v1/volumes?q="
    book_suffix= "isbn:" + booknumber
    title_suffix = "intitle:" + title_str
    author_suffix = "inauthor:" + author_str
    request_url = base_url + book_suffix if len(booknumber) == 13 else base_url + title_suffix +"&" + author_suffix 
    rawreply = requests.get(url= request_url)
    return rawreply.json()

@dataclass
class BookInfo:
    kind: str
    book_id: str
    title: str
    subtitle: str
    authors: str
    publisher: str
    publishedDate: str
    description: str
    isbn_13: str
    isbn_10: str
    isText : bool
    isImage: bool
    pageCount: int
    printType: str
    categories: list
    maturityRating: str
    language: str
    country: str
    isEbook: bool
    listPrice: float
    currencyCode: str
    retailPrice: float
    amountInMicros: int
    textToSpeechPermission: bool
    textSnippet: str

    @classmethod
    def from_dict(cls, data:dict) -> "BookInfo":
        kind_item = ''
        try:
            kind_item = data['items'][0]['kind']
        except KeyError as ke:
            kind_item = None
        id_item = ''
        try:
            id_item = data['items'][0]['id']
        except  KeyError as ke:
            id_item = None
        title_item = ''
        try:
            title_item = data['items'][0]['volumeInfo']['title']
        except KeyError as ke:
            title_item = None
        subtitle_item = ''
        try:
            subtitle_item = data['items'][0]['volumeInfo']['subtitle']
        except KeyError as ke:
            subtitle_item = None
        author_item = ''
        try:
            author_item = data['items'][0]['volumeInfo']['authors']
        except KeyError as ke:
            author_item = None
        publisher_item = ''
        try:
            publisher_item = data['items'][0]['volumeInfo']['publisher']
        except KeyError as ke:
            publisher_item = None
        publication_item= ''
        try:
            publication_item = data['items'][0]['volumeInfo']['publishedDate']
        except KeyError as ke:
            publication_item = None
        description_item=''
        try:
            description_item = data['items'][0]['volumeInfo']['description']
        except KeyError as ke:
            description_item = None

        isbn_13_item= ''
        try:
            isbn_13_item = data['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier']
        except  KeyError as ke:
            isbn_13_item = None

        isbn_10_item = ''
        try:
            isbn_10_item = data['items'][0]['volumeInfo']['industryIdentifiers'][1]['identifier']
        except KeyError as  ke:
            isbn_10_item = None

        isText_item = ''
        try:
            isText_item = data['items'][0]['volumeInfo']['readingModes']['text']
        except KeyError as ke:
            isText_item = None
        isImage_item= ''
        try:
            isImage_item =data['items'][0]['volumeInfo']['readingModes']['image']
        except KeyError as ke:
            isImage_item = None
        pageCount_item = ''
        try:
            pageCount_item = data['items'][0]['volumeInfo']['pageCount']
        except KeyError as ke:
            pageCount_item = None
        printType_item = ''
        try:
            printType_item = data['items'][0]['volumeInfo']['printType']
        except KeyError as ke:
            printType_item = None
        categories_item = ''
        try:
            categories_item =data['items'][0]['volumeInfo']['categories']
        except KeyError as ke:
            categories_item = None
        maturityRating_item = ''
        try:
            maturityRating_item = data['items'][0]['volumeInfo']['maturityRating']
        except KeyError as ke:
            maturityRating_item = None
        language_item = ''
        try:
            language_item = data['items'][0]['volumeInfo']['language']
        except  KeyError as ke:
            language_item =None

        country_item = ''
        try:
            country_item = data['items'][0]['saleInfo']['country']
        except KeyError as ke:
            country_item = None
        isEbook_item = ''
        try:
            isEbook_item = data['items'][0]['saleInfo']['isEbook']
        except KeyError as ke:
            isEbook_item = None
        amount_item = ''
        try:
            amount_item = data['items'][0]['saleInfo']['listPrice']['amount']
        except KeyError as ke:
            amount_item = None

        currencyCode_item = ''
        try:
            currencyCode_item = data['items'][0]['saleInfo']['listPrice']['currencyCode']
        except KeyError as ke:
            currencyCode_item = None

        retailPrice_item = ''
        try:
            retailPrice_item = data['items'][0]['saleInfo']['retailPrice']['amount']
        except KeyError as ke:
            retailPrice_item = None
        amountInMicros_item = ''
        try:
            amountInMicros_item = data['items'][0]['saleInfo']['offers'][0]['listPrice']['amountInMicros']
        except KeyError as ke:
            amountInMicros_item = None
        textToSpeechPermission_item = ''
        try:
            textToSpeechPermission_item = data['items'][0]['accessInfo']['textToSpeechPermission']
        except KeyError as ke:
            textToSpeechPermission_item = None

        textSnippet_item = ''
        try:
            textSnippet_item = data['items'][0]['searchInfo']['textSnippet']
        except KeyError as ke:
            textSnippet_item = None



        return cls(
                    kind=kind_item, book_id=id_item, title=title_item, subtitle = subtitle_item, authors=author_item, publisher= publisher_item, publishedDate= publication_item,
                    description=description_item, isbn_13=isbn_13_item, isbn_10=isbn_10_item, isText=isText_item,isImage=isImage_item, pageCount= pageCount_item, printType= printType_item, categories= categories_item, maturityRating=maturityRating_item, language= language_item, country = country_item,
                    isEbook= isEbook_item, listPrice= amount_item, currencyCode= currencyCode_item,retailPrice= retailPrice_item, amountInMicros= amountInMicros_item, textToSpeechPermission= textToSpeechPermission_item, textSnippet=textSnippet_item)




def retrieve_book_info(isbn, title, auth ):
    data = book_info(isbn, title, auth)
    return BookInfo.from_dict(data)





#s= retrieve_book_info('97818392189', "Data Engineering with Python", "Paul Crickard")
#print(s)
#print(asdict(s))
#m=retrieve_book_info('9781593279929', 'Automate the boring stuff', 'Al Sweigart')
#print(m)
#o = retrieve_book_info('9781491985571', "Web Scraping with Python", "Ryan Mitchell")
#print(o)
#a =  retrieve_book_info('978346204264', 'Die Große Verschleierung', 'Alice Schwarzer')
#print(a)
#d = retrieve_book_info('9783867890564','maria magdalena', 'Franz Xavier Kroetz')
#print(d)



def  add_meta_info(isbn_item: str = None, yearBought_item:str,yearRead_item:str, acquisitionMode_item:str, timesRead_item:str, stateBought_item:str, availabilityInfo_item:str  )-> dict:
    return {''isbn': isbn_item, 'yearBought': yearBought_item, 'yearRead': yearRead_item, 'acquistionMode': acquistionMode_item, 'timesRead': timesRead_item, 'statebought': stateBought_item, 'availabilityInfo': availabilityInfo_item}
