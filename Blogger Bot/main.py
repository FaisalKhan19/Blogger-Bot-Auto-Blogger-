from scraper import Scraper
import OpenAI

user = Scraper("https://www.reddit.com/", "Delicious_Hamster158", "old_mon36996", "AskReddit", "Q:\\Web scraping "
                                                                                               "udemy\\chromedriver.exe")
user.login()

prompts = user.scrape(20)

ans = OpenAI.get_res(prompts,"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")

for i, j in ans, prompts:
    print("Prompt is: ", j)
    print("---------------")
    print("Response got: ", i)
