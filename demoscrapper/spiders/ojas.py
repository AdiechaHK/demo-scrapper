import scrapy


class OjasSpider(scrapy.Spider):
    name = 'ojas'
    allowed_domains = ['ojas.gujarat.gov.in']
    start_urls = ['http://ojas.gujarat.gov.in/']
    custom_settings = {
    	"ROBOTSTXT_OBEY": False
    }

    def parse(self, response):
        list = response.css("#Job_Advt1_rowScrollingNw a")
        for anchor in list:
            url = anchor.css("::attr(href)").extract_first()
            yield scrapy.Request(response.urljoin(url), self.parseDetail)


    def parseDetail(self, response):
        yield {
            "advt_no": response.css("#lbladvtno *::text").extract_first(),
            "post_text": response.css("#lblPost *::text").extract_first(),
            "class": response.css("#lblPostClass *::text").extract_first(),
            "department": response.css("#lblDepartment *::text").extract_first(),
            "job_description": response.css("#lblJobDescription *::text").extract_first(),
            "payscale": response.css("#lblPayScale *::text").extract_first(),
            "probation": response.css("#lblProbation *::text").extract_first(),
            "age": response.css("#lblAgeDescription *::text").extract_first(),
            "ph_desc": response.css("#lblPHDesc *::text").extract_first(),
            "qualification": response.css("#lblQualificaitonDescription *::text").extract_first(),
            "experience": response.css("#lblExperienceDescription *::text").extract_first(),
            "other_condition": response.css("#lblOtherConditions *::text").extract_first()
        }
