import os.path as osp
import bs4
import requests
import re

warn_cnt = 0
def warn(msg):
    """Issue (and count) warnings"""
    global warn_cnt
    print("WARNING: {}".format(msg))
    warn_cnt += 1

def accepted_link(text):
    unaccepted_parts = ['contact.html', 'end-credits.html', '://tinyletter.com', '://pollenpub.com']
    for p in unaccepted_parts:
        if p in text:
            return False
    return True

BASE_URL = 'https://practicaltypography.com/'
START_PAGE = BASE_URL
resp = requests.get(START_PAGE)
soup = bs4.BeautifulSoup(resp.text, 'html.parser')

links = []
for link_tag in soup.find_all('a'):
    try:
        right_class = 'toc' in link_tag.get('class')
    except TypeError:
        right_class = False
    if right_class:
        link_text = link_tag.get('href')
        if accepted_link(link_text):
            links.append(link_text)

links = links

print ("Collected {} page links".format(len(links)))

PAGE_ORIG_FN = 'page_orig.html'
FILE_LIST_FN = 'clean_html_files.txt'
with open(FILE_LIST_FN,'w') as lf:
    for l in links:
        resp = requests.get(BASE_URL+l)
        resp.encoding = 'UTF-8' # server doesn't send utf-8 header, but pages ARE UTF-8

        with open(PAGE_ORIG_FN, 'w') as f:
            f.write(resp.text)


        # Inject BASE tag
        (re_res, re_cnt) = re.subn(r'(<title>)', r'<base href="https://practicaltypography.com/" target="_blank">\n\1',
                                   resp.text, 0, re.IGNORECASE)
        if re_cnt != 1:
            warn("Number of BASE tag injects was {}, not 1".format(re_cnt))

        # Inject base domain for "fonts" urls
        (re_res, re_cnt) = re.subn(r'(href=")(/fonts/equity)', r'\1https://practicaltypography.com\2',
                               re_res, 0, re.IGNORECASE)
        if re_cnt != 5:
            warn("Number of fonts injects was {}, not 5".format(re_cnt))

        # Remove the navigation
        m = re.search(r'<!-- top nav -->.*(</body>)', re_res, re.IGNORECASE+re.DOTALL)
        if m:
            # check the match is towards the end of the page/file
            distance_start = m.start()
            distance_end = len(re_res)-m.start()
            if distance_start>4200 and \
               distance_end<1200:
                re_res = re_res[0:m.start()] + m.expand(r'\1') + re_res[m.end():]
            else:
                warn("Navigation found, bt was not towards the end of the page - no navigation removed")
        else:
            warn("No navigation found")

        page_clean_name_html = '{base}_clean.html'.format(base=osp.splitext(l)[0])
        with open(page_clean_name_html, 'w') as f:
            f.write(re_res)

        lf.write(page_clean_name_html+'\n')
        print("Wrote PDF {}".format(page_clean_name_html))

print("-")
print("Wrote list of generated files to {}".format(FILE_LIST_FN))
if warn_cnt > 0:
    print("The conversion had {} warnings".format(warn_cnt))


