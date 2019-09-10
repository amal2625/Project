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


	def test(self, response):
		sub_name=response.xpath("//div[@class='SPList']/ul[@class='sp noselect']")
		# sub_names=sub_name.xpath("//ul[@class='sp noselect']")
		for test in sub_name:
			new_link=test.xpath(".//li[@class='sp-id']/p[@class='sp-name']/a/@href").extract_first()
			next_sub_page=response.urljoin(new_link)
			yield scrapy.Request(url=next_sub_page, callback=self.final_result)
		next_page=response.xpath("//div[@class='nav-page']")
		final_link=next_page.xpath("//a[@class='next-page button btn-small']/@href").extract_first()
		
		# if final_link is not None:
		# 	next_page_links=response.urljoin(final_link)
		# 	yield scrapy.Request(url=next_page_links, callback=self.test)
			
			

	def final_result(self, response):
		final_page=response.xpath("//div[@class='profile-container']")
		title=final_page.xpath(".//h1[@class='sp-title']/span/text()").extract_first()
		sub_title=final_page.xpath(".//h4/span[@class='sub']/text()").extract_first()
		primary_location_master_div=response.xpath("//div[@class='profile-details']")
		primary_location_label=primary_location_master_div.xpath("//table/tr[1]/td[1]/text()").extract_first()
		if primary_location_label == 'Primary location:':
			primary_location=primary_location_master_div.xpath("//table/tr[1]/td[2]/span[@itemprop='address']/span[@itemprop='addressLocality']/text()").extract_first()
			main_area=primary_location_master_div.xpath("//table/tr[2]/td[2]/a[@class='mainExp']/text()").extract_first()
		else:
			primary_location=''
			main_area=primary_location_master_div.xpath("//table/tr[1]/td[2]/a[@class='mainExp']/text()").extract_first()
		about=''
		website=''	
		language=''
		logo_url=final_page.xpath("..//div[@class='profile-image']/div[@class='image']/img/@data-original").extract_first()
		
		section_details_div=response.xpath("//div[@class='profile-content']/div[@class='section details']/table/tr")
		for section in section_details_div:
			label_names=section.xpath(".//td[1]/text()").extract_first()
			if label_names == 'About:':
				about=section.xpath(".//td[2]/p").extract()
				
			if label_names == 'Website:':
				website=section.xpath(".//td[2]/a/text()").extract_first()

			if label_names == 'Languages spoken:':
				language=section.xpath(".//td[2]/text()").extract_first()
		
		yield {
		'Logo Url':logo_url,
		'Title':title,
		'SubTitle':sub_title,
		'Primary Location':primary_location,
		'Main Area of Expertise':main_area,
		'About':about,
		'Website':website,
		'Language Spoken':language,
		'Page url':response.url
		}





			
        