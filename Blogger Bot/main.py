from Driver import Scraper
import OpenAI

user = Scraper()

user.login()

prompts = user.scrape(20)

ans = OpenAI.get_res(prompts,"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")

for i, j in ans, prompts:
    print("Prompt is: ", j)
    print("---------------")
    print("Response got: ", i)
