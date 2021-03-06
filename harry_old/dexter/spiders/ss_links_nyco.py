from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.http import Request
import re
from scrapy.exceptions import CloseSpider
import datetime 
import logging
import commands
from harry.dexter.items import Category, ProductItem, ColorSizeItem, CategoryItem
from debra.models import Brands, ProductModel, Items
import os, errno
from time import sleep
import copy
import urllib
from debra.modify_shelf import store_spec_product_categorization

#logging.basicConfig(format='%(message)s', level=logging.CRITICAL)

class SSNYCoSpider(CrawlSpider):
    name = "ssnyco"
    store_name = "New York & Company"
    HOME = "/Users/atulsingh/Documents/workspace2/"
    # stats
    all_items_scraped = set()
    invalid_links = 0

    count_scraped = 0
    urls_scraped = set()
    items_to_scrape = []
    items_scraped = []
    count = 0
    date = datetime.datetime.now()
    
    
    date_ = datetime.date(2012, 6, 29) #datetime.date.today() #(2012, 1, 31)

    start_night = datetime.time(0)
    mid_night = datetime.time(23, 59, 59)
    #day = datetime.timedelta(hours=23, minutes=59, seconds=59)
    d_start = datetime.datetime.combine(date_, start_night)
    d_end = datetime.datetime.combine(date_, mid_night)

    insert_date = date_ #datetime.date(2000, 1, 11)
    
    handle_httpstatus_list = [302]
    
    # prod url -> ss link url
    prod_link_to_ss_link_map = {}
    
    start_urls = []

    def __init__(self, *a, **kw):
        super(SSNYCoSpider, self).__init__(*a, **kw)
        try:
            if kw['single_url']:
                self._initialize_spec_urls(a[0], single_url=kw['single_url'])
            else:
                self._initialize_start_urls()
        except KeyError:
            self._initialize_start_urls()

    def _initialize_spec_urls(self, *a, **kw):
        print '==========INITIALIZATION======='
        one_url = kw['single_url']
        if one_url:
            url = a[0]
            self.start_urls.append(url)
    
    def _initialize_start_urls(self):
        #items_on_date = Items.objects.filter(insert_date__range = (self.d_start, self.d_end))
        items_on_date = Items.objects.all() 
        
        b = Brands.objects.get(name = self.store_name)
        print b
        items_of_brand = items_on_date.filter(brand = b)
        print "Items in Brands DB: " + str(len(items_of_brand))
        #print items_of_brand[0].pr_url
        #print items_of_brand[0].name
        #self.start_urls.append(items_of_brand[0].pr_url)
        #self.start_urls.append(items_of_brand[1].prod_url)

        #self.start_urls.append(items_of_brand[1].pr_url)
        #self.start_urls.append("http://www.express.com/striped-graphic-tee-come-away-with-me-47621-43/index.pro?productVariantId=329348&csename=Shopping.com&cid=1075&mr:referralI%20%20%20%20%20%20D=1538a1c2-c258-11e1-9e8b-001b2166c62d")
        #self.start_urls.append("http://www.express.com/chronograph-silicone-strap-watch-pitch-black-41065-845/control/show/3/index.pro")
        for item in items_of_brand:
            self.start_urls.append(item.pr_url)

    
    # checks if tok is present in sub
    def _contains(self, sub, tok):
        index = sub.find(tok)
        if index >= 0:
            return True
        else:
            return False

    # combine the array elements into a single string with 
    # provided delimiters
    def _combine(self, string_array, start_delim, end_delim):
        result = ""
        for i in range(0, len(string_array)):
            result += start_delim
            result += string_array[i]
            result += end_delim
            
        return result
            
            
    def _create_dir(self, fpath):
        print "Creating directory: ", fpath
        
        try:
            os.makedirs(fpath)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST:
                pass
            else: raise
            
        
    def _store_in_file(self, response, item_id):
        path_name = self.HOME + "/" + str(self.date.isoformat())
        self._create_dir(path_name)
        path_name += "/" + self.store_name + "/"
        self._create_dir(path_name)
        
        fname = path_name + str(item_id) + ".html"
        FILE = open(fname, 'w')
        FILE.write(str(response.body))
        FILE.close()
        
        
        
    def parse(self, response):
        url = response.url
        print "\n----Parse:: " + str(self.count) + " URL: " + str(url) + " Size of response: " + str(len(str(response.body)))
        #print str(response.body)
        
        if self._contains(str(url), '/nyco/prod/'):
            print "USEFUL URL " + str(url) 
            #if response.request.meta.get('redirect_urls'):
            #    print "Redirected from " + str(response.request.meta.get('redirect_urls')[0])
            print "\n---SCRAPING PAGE---\n"
            valid_prod, product = self.parse_nyco(response)
            print "\n---SCRAPING DONE---\n"
            if valid_prod:
                print "\n---VALID PRODUCT---\n"
            else:
                print "\n---NO, IT's NOT A VALID PRODUCT---\n"
                
        self.count += 1
        print "Total pages scraped " + str(self.count_scraped) + " Total URLS " + str(self.count) + \
              " Total invalid links " + str(self.invalid_links)
        valid, url_to_follow = self.follow_forward_link(response)
        if valid:
            #print "Following " + str(url_to_follow) + " \nCrawled: " + str (url)
            self.prod_link_to_ss_link_map[urllib.unquote(url_to_follow)] = url
            #print self.prod_link_to_ss_link_map
            yield Request(url_to_follow, callback=self.parse)
                
        #return []

    def follow_forward_link(self, response):
        #start_ind = urls_to_follow[0].find('url=')
        #url_start = urls_to_follow[0][start_ind+4:]
        start_ind = response.body.rfind('redirect=')
        if start_ind >= 0:
            print "Found index for 'redirect'"
            url_start = response.body[start_ind+9:]
        else:
            print "No, didn't find redirect, now looking for 'url'"
            start_ind = response.body.rfind('url=')
            print "Start index " + str(start_ind)
            if start_ind >= 0:
                url_start = response.body[start_ind+4:]
        if start_ind < 0:
            return (False, None)
        end_ind_1 = url_start.find(" ")
        end_ind_2 = url_start.find("'")
        if end_ind_1 > end_ind_2:
            end_ind = end_ind_2
        else:
            end_ind = end_ind_1
        url_ = url_start[:end_ind]
        url__ = urllib.unquote(url_)#url_.decode('utf-8')
        #print "FORWARDED URL: " + str(url_)
        if self._contains(url__, 'http://'):
            print "FORWARDED URL: " + str(url__)
        
            return (True, url__)
        else:
            return (False, url__)
   
    def _helper_check(self, hxs, tag, tag_value):
        cmd_string = '//' + tag + '="' + tag_value + '"'
        result = hxs.select(cmd_string).extract()
        if result == 'False':
            print "\t Problem with " + tag + " " + tag_value
        return result
    
    def check_shelfit_validity(self, response):
        hxs = HtmlXPathSelector(response)
        print response.url

        # Size
        #d.getElementById("SelectSize_0");
        self._helper_check(hxs, "@class", "expandMe")
        
        # Color
        #d.getElementById("color-picker");
        # grand kids must have <a...
        self._helper_check(hxs, "@class", "selectedColor")
        
        # Img url
        #getElementById('productImage').src
        if (self._helper_check(hxs, "@id", "cat-prod-flash-alt-views")):
            children = hxs.select('//@id="cat-prod-flash-alt-views"')

        # quantity
        #d.getElementById('quantity').value;
        self._helper_check(hxs, "@id", "quantity")
        
        # product id
        #d.getElementById('productId').value;
        self._helper_check(hxs, "@id", "productId")
        
        # d.getElementsByTagName('meta');
        # URL
        # meta: og-url
        self._helper_check(hxs, "@property", "og:url")
        # meta: og-title
        # prod name
        self._helper_check(hxs, "@property", "og:title")

   
    def parse_nyco(self, response):
        #self.check_shelfit_validity(response)
        #return
        hxs = HtmlXPathSelector(response)
        
        # find name of item
        item_name_path = hxs.select('//h1/text()')
        if len(item_name_path) == 0:
            self.invalid_links += 1
            return (False, None)
        item_name = item_name_path.extract()
        logging.critical("Name: " + str(item_name))
                
        self.count_scraped += 1
        
        ''' 
        PLAYING NICE: sleeping for 1min after crawling every 100 pages
        '''
        if self.count_scraped % 100 == 0:
            sleep(0) # sleep for 1 mins for express
            
        can_url_path = hxs.select('//link[@rel="canonical"]/@href')
        if len(can_url_path) > 0:
            prod_url = can_url_path.extract()[0]
        else:
            prod_url = response.url
        logging.critical("PRODUCT URL:" + str(prod_url) + " TITLE " + str(item_name) + " TOTAL SO FAR " + str(self.count_scraped))

        # find gender
        gender = 'F'
        logging.critical("Gender: " + gender)
        
        
        # find price and sale price
        item_id_, price_, sale_price_ = self._find_price(hxs, prod_url)
        
        if item_id_ in self.all_items_scraped:
            print "RETURNING since we have already scraped " + str(item_id_)
        
        self.all_items_scraped.add(item_id_)
                
        logging.critical("ITEM_ID " + str(item_id_) + " PRICE " + str(price_) + " SALE PRICE " + str(sale_price_))
        
        # extract image URL
        img_str = re.findall('strLarge = ["\w\d\/:_\$.?]+', str(response.body))
        prod_img_url = ""
        if len(img_str) > 0:
            img_str_ = img_str[0]
            img_str_parts = img_str_.split()
            if len(img_str_parts) > 2:
                prod_img_url = img_str_parts[2].strip('"')
        if prod_img_url == "":
            logging.critical("PROBLEM with Image URL for " + str(response.url))
        logging.critical("Image URL: " + str(prod_img_url))


        # find description and keywords: these will be useful in categorization
        desc = hxs.select('//p[@class="itemstyle_pdp"]/span[@class="details"]/text()').extract()
        logging.critical("Description: ")
        logging.critical(desc)
        prod_desc = desc
        
        # promo text
        promo_str = ""

        

        product, created_new = self._create_product_item(item_name[0], int(item_id_), str(prod_url), price_, \
                                            sale_price_, gender, str(prod_img_url), promo_str, prod_desc)
        
        if product == None:
            logging.critical("PROBLEM: product is None for URL " + str(response.url))
        
        cat1_path = hxs.select('//ul[@id="leftnav"]/li[@class="selected"]/a/span/text()').extract()    
        
        cat1 = "Nil"
        cat2 = "Nil"
        cat3 = "Nil"
        
        if len(cat1_path) > 0:
            cat1 = cat1_path[0].strip()
       
        print cat1
        print cat2 
        store_spec_product_categorization(product, cat1, cat2, cat3)
        print "Cat1 " + str(product.cat1) + " Cat2 " + str(product.cat2) + " Cat 3" + str(product.cat3)
        #self._create_category(product, categories)


        #self._store_in_file(response, item_id_)
        #raise CloseSpider('Blah')
        logging.critical("Total unique items: " + str(len(self.all_items_scraped)) + " we have scraped so far: " +\
                          str(self.count_scraped) + " Unique URLs scraped: " + str(len(self.urls_scraped)))
        #raise SystemExit
        
        return (True, product)
        
        
    def process_links_none(self, links):
        print "Links from BVReviews: " + str(links)
        return set()
    
    def process_links_sub(self, links):
        return links
		
    def find_itemid_in_url(self, url_str):
        end = url_str.rfind('-')
        s1 = url_str[0:end]
        start = s1.rfind('-')
        itemid = s1[start+1: len(s1)]
        #print itemid
        #raise SystemExit
        return itemid


  
    def avoid_redirection(self, request):
        request.meta.update(dont_redirect=True)
        #request.meta.update(dont_filter=True)
        return request
    
    def _get_color_size_array(self, response):
        colorToSizeArray = re.findall('colorToSize[\w\d\[\]\\\',=\s]+;', str(response.body))
        #print colorToSizeArray
        total = len(colorToSizeArray)
        colorSizeMapping = {}
        
        for i in range(0, total):
            mapping_var = colorToSizeArray[i]
            #print mapping_var
            '''
            mapping_var is a string, e.g.: colorToSize42466Array['ENSIGN'] = ['X Small', 'Small', 'Large'];
            '''
            square_brk_left = mapping_var.find('[')
            square_brk_right = mapping_var.find(']')
            #print "Square_left " + str(square_brk_left) + " Square_right " + str(square_brk_right)
            color = mapping_var[square_brk_left+2: square_brk_right-1]
            #print color
            
            sizes_str = mapping_var[square_brk_right+5: len(mapping_var)]
            #print sizes_str
            
            num_sizes = sizes_str.count(',') + 1
            #print "Num sizes " + str(num_sizes)
            size = []
            for j in range(0, num_sizes):
                single_quote_left = sizes_str.find("\'")
                #print "Quoteleft " + str(single_quote_left)
                remaining_sizes_str = sizes_str[single_quote_left+1: len(sizes_str)]
                #print "Remaining " + remaining_sizes_str
                single_quote_right = remaining_sizes_str.find("\'")
                #print "QuoteRight " + str(single_quote_right)
                size_elem = remaining_sizes_str[0: single_quote_right]
                #print "Size_elem " + size_elem
                size.append(size_elem)
                sizes_str = sizes_str[single_quote_right+ single_quote_left + 3: len(sizes_str)]
            #print size
            colorSizeMapping[color] = copy.deepcopy(size)
    
        return colorSizeMapping
    
    def _create_product_item(self, name, prod_id, prod_url, price, saleprice, gender, img_url, promo_text, prod_desc):
        from django.core.exceptions import ObjectDoesNotExist

        b = Brands.objects.get(name = self.store_name)
        
        existing_item = ProductModel.objects.filter(brand = b).filter(idx = prod_id)
        print existing_item
        if len(existing_item) > 0:
            print "Item " + str(existing_item[0]) + " EXISTS. Not creating new one. Returning...."
            return (existing_item[0], False)
             
        logging.critical("CREATE_PRODUCT OBJ: foreign key " + str(b))
        item = ProductModel(brand = b, 
                            idx = prod_id,
                            name = name,
                            prod_url = prod_url,
                            price = price,
                            saleprice = saleprice,
                            promo_text = promo_text,
                            gender = gender,
                            img_url = img_url,
                            description = prod_desc,
                            insert_date = self.insert_date,)

        #print item
        item.save()
        print "CREATING NEW PRODUCT MODEL OBJ"
        #return (item.save(), True)
        return (item, True)

    def _create_color_size(self, product, color_array, size_array):
        c_size = len(color_array)
        s_size = len(size_array)
        # pick the minimum
        min = c_size
        if c_size > s_size:
            min = s_size
        for i in range(0, min):
            colorsize = ColorSizeItem()
            colorsize['product'] = ProductModel.objects.get(pk=product.id)
            colorsize['color'] = color_array[i]
            colorsize['size'] = size_array[i]
            colorsize.save()
        
        
    
    def _create_category(self, product, categories):
        for cat in categories:
            category = CategoryItem()
            category['product'] = ProductModel.objects.get(pk=product.id)
            category['categoryId'] = 0
            category['categoryName'] = cat
            category.save()

    def _find_price(self, hxs, url):
        price = 0
        sale_price = 0
        item_id = -1
        style_txt_array = hxs.select('//p[@class="itemstyle_pdp"]/text()').extract()
        if len(style_txt_array) > 0:
            style = style_txt_array[0]
            vals = style.split()
            if len(vals) > 1:
                item_id = int(vals[1].strip('.'))
        
        if item_id == -1:
            print "ITEM_ID NOT FOUND for url: " + str(url)
        return (item_id, price, sale_price)
        
        
        
        
