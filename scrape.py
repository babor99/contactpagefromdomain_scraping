import httpx
from bs4 import BeautifulSoup
import re

search_list = ['contact-us', 'Contact-Us', 'contactus', 'ContactUs', 'contact', 'Contact', 'Contact-us', ]

mystring = """
            Hi, this is my string and in this string,
            I will write all my routes. Like if a website has something robots.txt or 
            sitemap.xml. I will do these things here in this string. So my robots.txt starts here:
            User-agent: *
            Disallow: /gp/richpub/listmania/createpipeline
            Disallow: /gp/content-form
            Disallow: /gp/pdp/invitation/invite
            Disallow: /gp/customer-reviews/common/du
            Disallow: /gp/customer-reviews/write-a-review.html
            Disallow: /gp/associations/wizard.html
            Disallow: /gp/music/clipserve
            Disallow: /gp/customer-media/upload
            Disallow: /gp/history
            Disallow: /gp/item-dispatch
            Disallow: /gp/Contact/order/handle-buy-box.html
            Disallow: /gp/recsradio
            Disallow: /gp/slredirect
            """
mystring2 = """
            Hi, this is my string and in this string,
            I will write all my routes. Like if a website has something robots.txt or 
            sitemap.xml. I will do these things here in this string. So my robots.txt starts here:
            User-agent: *
            Disallow: /gp/richpub/listmania/createpipeline
            Disallow: /gp/content-form
            Disallow: /gp/pdp/invitation/invite
            Disallow: /gp/customer-reviews/common/du
            Disallow: /gp/customer-reviews/write-a-review.html
            Disallow: /gp/associations/wizard.html
            Disallow: /gp/music/clipserve
            Disallow: /gp/customer-media/upload
            Disallow: /gp/history
            Disallow: /gp/item-dispatch
            Disallow: /gp/dmusic/order/handle-buy-box.html
            Disallow: /gp/recsradio
            Disallow: /gp/slredirect
            Disallow: /dp/shipping/
            Disallow: /dp/twister-update/
            Disallow: /dp/manual-submit/
            Disallow: /dp/e-mail-friend/
            Disallow: /dp/product-availability/
            Disallow: /dp/rate-this-item/
            Disallow: /gp/contactus/wishlist/*/reserve
            Disallow: /gp/structured-ratings/actions/get-experience.html
            Disallow: /Contactus/twitter/
            Disallow: /gp/socialmedia/giveaways
            Disallow: /contact/host/setup/
            Disallow: /ss/ContactUs/lighthouse/
            Disallow: /ospublishing/story/*
            Disallow: /gp/aw/ol/
            Disallow: /gp/promotion/
            Disallow: /hz/leaderboard/top-reviewers/
            Disallow: /hz/help/contactUs/*/message/$
            Disallow: /gp/aw/shoppingAids/
            Disallow: /rss/people/*/reviews
            Disallow: /gp/pdp/rss/*/reviews
            Disallow: /gp/cdp/member-reviews/
            Disallow: /gp/aw/cr/
            Disallow: */sim/B001132UEE
            Allow: /gp/aag/main?*seller=ABVFEJU8LS620
            Disallow: /gp/pdp/profile/
            Disallow: /gp/help/customer/express/c2c/
            Disallow: /slp/*/b$
            Disallow: /hz/contact-us/ajax/initiate-trusted-contact/
            Disallow: /gp/video/api
            Disallow: /hp/video/api
            Disallow: /gp/video/mystuff
            Disallow: /hp/video/mystuff
            Disallow: /gp/video/profiles
            Disallow: /hp/video/profiles
            """

def scrape():
    url = 'https://www.rokomari.com'
    res = httpx.get(url)
    print('res: ', res)
    soup = BeautifulSoup(res.content, 'html.parser')
    # print(soup.prettify())
    print('res: ', res)
    href_elem = soup.find(href=re.compile('(contact-?us)|(contact-?)', re.I))
    print('href_elem: ', href_elem)
    if href_elem:
        href = href_elem.attrs['href']
        if url in href:
            contact_page = httpx.get(href)
            print('contactpage: ', BeautifulSoup(contact_page.content, 'html.parser').prettify())
            print('full url: ', href)
        else:
            if url.endswith('/'):
                full_url = url + href.replace('/', '', 1)
                contact_page = httpx.get(full_url)
                print('contactpage: ', BeautifulSoup(contact_page.content, 'html.parser').prettify())
                print('full url: ', full_url)



if __name__ == '__main__':
    scrape()