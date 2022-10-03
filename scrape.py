import httpx
from bs4 import BeautifulSoup
import re


search_urls = ['contact-us', 'contactus', 'Contact-Us', 'ContactUs', 'Contact-us', 'contact', 'Contact', ]


def alternate_scrape(url: str):
    return_url = None
    for search_url in search_urls:
        if url.endswith('/'):
            full_url = url + search_url
        else:
            full_url = url + '/' + search_url

        res = httpx.get(full_url)
        if str(res.status_code) == '200':
            return_url = full_url
            break

    return return_url


def getFullUrlFromUrlAndHref(url: str, href: str) -> str:
    if url in href:
        return href
    else:
        if url.endswith('/'):
            return url + href.replace('/', '', 1)
        else:
            return url + href




# url = 'https://www.rokomari.com'
# url = 'https://championplumbingandrooter.com'
# url = 'https://www.alibaba.com'
# url = 'https://www.amazon.com'
# url = 'https://getintopc.com'
# url = 'https://filehippo.com/'
# url = 'https://www.airindia.in'
url = 'https://www.biman-airlines.com'



def scrape(url: str) -> str:
    return_url = None
    res = httpx.get(url)
    print('res: ', res)
    if str(res.status_code) == '200':
        soup = BeautifulSoup(res.content, 'html.parser')
        href_elements = soup.find_all(href=re.compile('(contact-?us)|(contact-?)', re.I))
        elements_len = len(href_elements)
        if  elements_len == 1:
            href = href_elements[0].attrs['href']
            return_url = getFullUrlFromUrlAndHref(url, href)
        elif elements_len > 1:
            content = ""
            for elem in href_elements:
                content += str(elem)
            soup2 = BeautifulSoup(content, 'html.parser')
            href_element = soup2.find(href=re.compile('contact-?us', re.I))
            if href_element:
                href = href_element.attrs['href']
                return_url = getFullUrlFromUrlAndHref(url, href)
            else:
                href_element = soup2.find(href=re.compile('contact-?', re.I))
                if href_element:
                    href = href_element.attrs['href']
                    return_url = getFullUrlFromUrlAndHref(url, href)
                else:
                    return_url = None
        else:
            return_url = alternate_scrape(url)

    else:
        return_url = alternate_scrape(url)

    if return_url is not None:
        return return_url
    else:
        raise PermissionError("The website can't be crawled or perhaps provided url is invalid.")



if __name__ == '__main__':
    outcome = scrape(url)
    print('outcome: ', outcome)

