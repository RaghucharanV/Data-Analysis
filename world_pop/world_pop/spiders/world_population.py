import scrapy


class WorldPopulationSpider(scrapy.Spider):
    name = "world_population"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/"]

    def parse(self, response):
        for row in response.css("table#popbycountry tbody tr"):
            data = row.css("td::text").getall()
            country = row.css("td a::text").getall()

            yield {
                "country ": country,
                'Population': data[1],
                "yearly change": data[2],
                "Net change":data[3],
                "Density":data[4],
                "Land Area (Km2)": data[5],
                "Migrants(n)":data[6],
                "Fert_Rate": data[7],
                "Med_Age":data[8],
                "Urban_Pop":data[9],
                "World_share":data[10]
            }
