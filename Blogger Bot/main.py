from Driver import Scraper
import OpenAI

user = Scraper()

user.login()

prompts = user.scrape(20)
api_key = "Your api key for open ai(visit-https://platform.openai.com/account/api-keys)"
ans = OpenAI.get_res(prompts,api_key)

for i, j in ans, prompts:
    print("Prompt is: ", j)
    print("---------------")
    print("Response got: ", i)
