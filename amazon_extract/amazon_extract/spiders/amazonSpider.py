import scrapy
import sys

from amazon_extract.items import AmazonExtractItem
def startUrl():
	urls = []
	f = open("isbn.dat","r")
	for line in f:
		urls.append("http://amazon.fr/s/?field-keywords="+line)
	return urls
class AmazonSpider(scrapy.Spider):
	name = "amazon"
	allowed_domains = ["amazon.fr"]
	start_urls = startUrl()

	def parse(self, response):
		#ToDo : Je ne trouve pas le moyen d'aller chercher le lien vers la version dans un autre format
		# le node xpath n'est pas detecter
		print "\n\n"
		print(response.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@title').extract_first())
		print "\n\n"
		print(response.xpath('//a[@class="a-link-normal   a-text-normal"]/@title').extract_first())
		print "\n\nOther Format"
		print (response.css('a.a-size-small:nth-child(7)').extract())
		print "\n\n"
		url = response.xpath('//li[@id="result_0"]/div/div/div/div/div/a/@href').extract_first()
#		yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		item = AmazonExtractItem()
		item['title'] = response.xpath('//span[@id="productTitle"]/text()').extract_first()
		item['autor'] = response.xpath('//div[@id="byline"]/span/a/text()').extract_first()
		i = 0
		for sel in response.xpath('//div[@id="detail_bullets_id"]/table/tr/td/div/ul/li'):
			if(i == 0):
				item['pages'] = sel.xpath('text()').extract_first()
			elif(i == 5):
				item['isbn'] = sel.xpath('text()').extract_first()
			i+=1
		yield item
