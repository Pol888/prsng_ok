from bs4 import BeautifulSoup
from selenium import webdriver
import time

def ok(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        b = 0

        while True:
            time.sleep(5)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            comments = soup.find('div', class_="vp-chat_cnt").find_all('div', class_="vp-chat_i show-on-hover")
            a = len(comments)
            c = a - b
            if c > 0:
                for i in comments[-(c):]:
                    id = str(i).split('"')[5]
                    link = i.find('a').get('href')
                    name = i.find(class_="vp-chat_i_n o ellip-i").text
                    com = i.find(class_="vp-chat_i_tx textWrap").text

                    print(id, link, name, com)



                    with open("1.txt", "a", encoding="utf-8") as file:
                        file.write(f'{id}||{link}||{name}||{com}\n')
            b = a


    except:
        print('Ошибка высокого уровня')





    driver.close()


def main():
    inpt = input('Вставьте ссылку и нажмите Enter: ')
    ok(inpt)



if __name__ == '__main__':
    main()