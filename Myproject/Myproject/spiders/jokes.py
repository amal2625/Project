import scrapy

class JokesSpider(scrapy.Spider):
	name = 'jokes'
	start_urls = [
	'http://www.laughfactory.com/jokes/family-jokes'
	]

	def parse(self, response):

		product_name=response.xpath("//div[@class='jokes']")

		for jok in product_name:
			yield {
				'joke_test': jok.xpath(".//div[@class='joke-text']/p").extract_first()
			}
		next_page=response.xpath("//li[@class='next']/a/@href").extract_first();
		if next_page is not None:
			next_page_link= response.urljoin(next_page)
			yield scrapy.Request(url=next_page_link, callback=self.parse)

			

			
        