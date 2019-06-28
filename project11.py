from splinter  import Browser
from bs4 import BeautifulSoup
browser = Browser('chrome')

#driver = webdriver.Chrome()

name = input("Enter The SOurece")
name1 = input("ENter TheDestination")
#x=driver.get("https://maps.google.com")
url=r'https://www.google.com/maps/dir/'+name+r'/'+name1+r'/@22.5570559,88.0358596,11z/data=!3m1!4b1!4m5!3m4!1s0x39f88249be00ca5f:0x3f5496c42f4bd6e8!8m2!3d22.5957689!4d88.2636394'
browser.visit(url)
x = browser.html
#user = x.find_element_by_tag_name('span')# class="section-trip-summary-subtitle"'.format(name))
#print(user)
soup = BeautifulSoup(x,'html.parser')
p  =soup.find_all('span', {'class':"section-trip-summary-subtitle"}) #'class'="dealy-medium")
print(p)
#print(a)
for l in p:
    if p.get('span '):
        print(l)
        
for i in soup.find_all('span'):
    if i.get('jstcache')== 1312:
        print(i)
#for i in p:
 #   k=p.has_key('class = delay-medium')


#print(x)
