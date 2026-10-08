import asyncio
import logging

import aiohttp

NCT_API = "https://graph.nhaccuatui.com/api/v1/search/song"
TIMEOUT = aiohttp.ClientTimeout(total=10)

log = logging.getLogger(__name__)


async def search_music(session, keyword, pagesize=10):
    params = {
        "keyword": keyword,
        "pageindex": 1,
        "pagesize": pagesize,
        "correct": "true",
    }

    try:
        async with session.post(NCT_API, params=params, timeout=TIMEOUT) as response:
            response.raise_for_status()
            return await response.json(content_type=None)
    except (aiohttp.ClientError, asyncio.TimeoutError, ValueError):
        log.exception("NCT search failed: %s", keyword)
        return None