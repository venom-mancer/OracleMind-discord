import json
import asyncio
import aiohttp

async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_all_json(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(fetch_json(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        return responses

# example usage
async def playerinfo(query):
    urls = [
        'https://api.opendota.com/api/players/{}'.format(query),
        'https://api.opendota.com/api/players/{}/wl'.format(query),
        'https://api.opendota.com/api/players/{}/peers'.format(query)
    ]
    json_responses = await fetch_all_json(urls)
    json_object = json.dumps(json_responses, indent=4)
 
    with open("match_result.json", "w") as outfile:
        outfile.write(json_object)





