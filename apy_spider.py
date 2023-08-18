import scrapy


class ApySpider(scrapy.Spider):
    name = 'apy_scraper'
    allowed_domains = ['http://qx-020264.local']
    start_urls = ['http://qx-020264.local:8080/api/v1/']

    def start_requests(self):
        # Define a list of URLs with variables
        urls = []

        for url in urls:
            if "{" in url and "}" in url:
                # If URL contains variables, call a separate method to handle it
                yield scrapy.Request(url=url, callback=self.parse_url)
            else:
                # If URL does not contain variables, call parse method
                yield scrapy.Request(url=url, callback=self.parse)

    def handle_variable_url(self, url_template):
        # Extract variable names from URL
        variable_names = re.findall(r'{(.*?)}', url_template)

        # Define some example values for the variables
        variable_values = ["value1", "value2", "value3"]

        for value in variable_values:
            # Replace each variable with an current value
            url = url_template.replace("{" + variable_names[0] + "}", value)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Parse the API response
        data = response.json()

        # Process the data
        for item in data:
            ..
