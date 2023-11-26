#using Professor's example from GitHub
import asyncio
import aiohttp
import json
import requests

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

def synch_main():
    result = []
    for r in resources:
        t = requests.get(r["url"])
        t = t.json()
        result2 = {"resource": r["resource"],"data": t}
            
        result.append(result2)

    full_result = {}
    for response in result:
        full_result[response["resource"]] = response["data"]

    print("\nFull Result = ", json.dumps(full_result, indent=2))

synch_main()

