import urllib.request
import json
import re

client_id = "5VCE_BxiQ5d05HLztHL7"
client_secret = "BFL_7DhzxJ"

def get_books(query,display):
    
    encText = urllib.parse.quote(query)
    idx = 0
    #display = 100
    sort = "sim" # sim(유사도순), date(출간일순), count(판매량순)
    
    book_list=[]

    url = "https://openapi.naver.com/v1/search/book?query=" + encText \
            +"&display=" + str(display) \
            +"&sort=" + sort 
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_dict = json.loads(response_body.decode('utf-8'))
        items = response_dict['items']
        for item_index in range(0,len(items)):
            remove_tag = re.compile('<.*?>')
            title = re.sub(remove_tag, '', items[item_index]['title'])
            link = items[item_index]['link']
            image = items[item_index]['image']
            pre_author = re.sub(remove_tag, '', items[item_index]['author'])
            author = pre_author.replace('|',', ')
            price = items[item_index]['price']
            discount = items[item_index]['discount']
            publisher = items[item_index]['publisher']
            pre_isbn =  items[item_index]['isbn']
            isbn = pre_isbn.replace(' ','')
            pre_description = re.sub(remove_tag, '', items[item_index]['description'])
            pre_description2 = pre_description.replace('\n','')
            description = pre_description2.replace('&#x0D;','')
            pubdate = items[item_index]['pubdate']
            book_dict={'title':title,'link':link,'image':image,'author':author,\
                'price':price,'discount':discount,'publisher':publisher,\
                'isbn':isbn,'description':description,'pubdate':pubdate}
            book_list.append(book_dict)
            idx += 1
            
    else:
        print("Error Code:" + rescode)
    
    return book_list
        
