import scrapy

class TestSpider(scrapy.Spider):
	name = 'test'
	start_urls = [
	'https://www.globaltrade.net/expert-service-provider.html'
	]

	def parse(self, response):

		product_name=response.xpath("//div[@class='countrySelect']")

		contry_url=response.xpath("//li/a[@class='sp_country_71']/@href").extract_first()
		if contry_url is not None:
			next_page_link=response.urljoin(contry_url)
			yield scrapy.Request(url=next_page_link, callback=self.test)


		# for country_name in product_name:
		# 	yield {
		# 		'urls': country_name.xpath("//li/a[@class='sp_country_71']/@href").extract_first()
		# 	}




		# for jok in product_name:
		# 	yield {
		# 		'joke_test': jok.xpath(".//div[@class='joke-text']/p").extract_first()
		# 	}
		# next_page=response.xpath("//li[@class='next']/a/@href").extract_first();
		# if next_page is not None:
		# 	next_page_link= response.urljoin(next_page)
		# 	yield scrapy.Request(url=next_page_link, callback=self.parse)

	def test(self, response):
		sub_name=response.xpath("//div[@class='SPList']/ul[@class='sp noselect']")
		# sub_names=sub_name.xpath("//ul[@class='sp noselect']")
		for test in sub_name:
			new_link=test.xpath(".//li[@class='sp-id']/p[@class='sp-name']/a/@href").extract_first()
			next_sub_page=response.urljoin(new_link)
			yield scrapy.Request(url=next_sub_page, callback=self.final_result)

	def final_result(self, response):
		image_url=response.xpath("//div[@class='profile-container']")
		first_section=image_url.xpath(".//h1[@class='sp-title']/span").extract_first();

		yield {
		'Title':first_section
		}





			
        