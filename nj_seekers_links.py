from bs4 import BeautifulSoup
import requests

MAIN_URL = 'http://www.novjob.ru/'

number_of_pages = 0

CRAWLED_RLINKS = []


def get_page_content(url):
    page_response = requests.get(url, timeout=5)
    page_content = page_response.text
    return page_content


def get_page_links(content):
    soup = BeautifulSoup(content, 'lxml')
    links_short = soup.select('.hdr')
    links = []
    for short_link in links_short:
        links.append(MAIN_URL+str(short_link.attrs['href'])[2:])
    return links


def fill_crawled_links(links_on_cpage):
    for link in links_on_cpage:
        CRAWLED_RLINKS.append(link)
        print(f'Crawled: {link}')


def get_data(content):
    soup = BeautifulSoup(content, 'lxml')
    tds = soup.find('div', class_='osn').find_all('td')
    for i, td in enumerate(tds):
        print('------------------------------------------------------------------------------')
        print(f'|||{i}||| TD is: {td}')
        print('------------------------------------------------------------------------------')
        
    return tds


def main():
    number_of_pages = input('До какой страницы парсим?')

    for page_index in range(1, int(number_of_pages)+1):

        page_link = MAIN_URL+'cv.php?page=' + str(page_index)

        page_content = get_page_content(page_link)
        links_on_cpage = get_page_links(page_content)
        fill_crawled_links(links_on_cpage)
    for i, link in enumerate(CRAWLED_RLINKS):
        page_content = get_page_content(link)
        data = get_data(page_content)



    input('Press Enter to exit...')


if __name__ == '__main__':
    main()
