#using Professor's example from GitHub
import asyncio
import aiohttp
import json

resources = [
    {
        "resource": "review",
        "url": 'https://review-management-402504.ue.r.appspot.com/recipe/21'
    },
    {
        "resource": "recipe",
        "url": 'http://54.85.211.51:8011/recipes?objects_filter=sarah_m'
    },
    {
        "resource": "users",
        "url": 'http://ec2-3-89-127-211.compute-1.amazonaws.com:8011/users/sarah_m',
    }
]


async def fetch(session, resource):
    url = resource["url"]
    print("Calling URL = ", url)
    async with session.get(url) as response:
        t = await response.json()
        print("URL ", url, "returned", str(t))
        result = {
            "resource": resource["resource"],
            "data": t
        }
    return result


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch(session, res)) for res in resources]
        responses = await asyncio.gather(*tasks)
        full_result = {}
        for response in responses:
            full_result[response["resource"]] = response["data"]

        print("\nFull Result = ", json.dumps(full_result, indent=2))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())