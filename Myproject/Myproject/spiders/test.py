import scrapy

class TestSpider(scrapy.Spider):
	name = 'test'
	start_urls = [
	'https://www.globaltrade.net/expert-service-provider.html'
	]

	def parse(self, response):

		product_name=response.xpath("//div[@class='countrySelect']")

		for country_name in product_name:
			yield {
				'urls': country_name.xpath("//li/a/@href").extract_first()
			}




		# for jok in product_name:
		# 	yield {
		# 		'joke_test': jok.xpath(".//div[@class='joke-text']/p").extract_first()
		# 	}
		# next_page=response.xpath("//li[@class='next']/a/@href").extract_first();
		# if next_page is not None:
		# 	next_page_link= response.urljoin(next_page)
		# 	yield scrapy.Request(url=next_page_link, callback=self.parse)

			

			
        