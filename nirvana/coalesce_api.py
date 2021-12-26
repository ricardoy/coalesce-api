import asyncio
import json
import logging
from dataclasses import dataclass
from typing import Union, Callable

from nirvana.clients.request_client import RequestProtocol
from nirvana.coalesce_stragety import AbstractCoalesce

logger = logging.getLogger(__name__)


@dataclass
class RequestData:
    url: str
    method: str


class CoalesceApi:
    def __init__(
        self,
        request: RequestProtocol,
        coalesce_factory: Callable[[], AbstractCoalesce],
        urls: list[RequestData],
    ):
        self.request = request
        self.coalesce_factory = coalesce_factory
        self.urls = urls

    async def search(self, member_id: int) -> dict[str, Union[int, float]]:
        coalesce_strategy = self.coalesce_factory()
        tasks = []
        for url_formatter in self.urls:
            url = url_formatter.url.format(member_id=member_id)
            method = url_formatter.method
            task = asyncio.create_task(self.request(url=url, method=method))
            tasks.append((task, url, method))

        for task, url, method in tasks:
            r = await task
            if r.status == 200:
                j = json.loads(r.content.decode("utf-8"))
                coalesce_strategy.add_data(j)
            else:
                logger.error(f"Error accessing {url} - method: {method}")

        return coalesce_strategy.get_coalesced()
