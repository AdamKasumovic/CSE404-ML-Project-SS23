from selenium import webdriver
import urllib.request

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

# replace with path to your chromedriver
driver = webdriver.Chrome(executable_path=r'C:\Users\Adam Kasumovic\Desktop\chromedriver.exe', options=options)
driver.get('https://pokemondb.net/pokedex/national')

card_pics = driver.find_elements_by_xpath("//img[@class='img-fixed img-sprite']")
card_pics_links = [i.get_attribute('src') for i in card_pics]
print(len(card_pics_links))

driver.close()

# calling urlretrieve function to get resource
for link in card_pics_links:

    urllib.request.urlretrieve(link, '../data/images/'+ link[link.rfind('/')+1:link.rfind('.')] + '.png')