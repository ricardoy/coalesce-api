from dataclasses import dataclass
from typing import Any, Protocol, Optional

import aiohttp
from aiohttp.web import HTTPRequestTimeout, HTTPInternalServerError


@dataclass
class Response:
    status: int
    content: bytes


# pylint: disable=unused-argument
class RequestProtocol(Protocol):
    async def __call__(
        self,
        url: str,
        method: str,
        headers: Optional[dict] = None,
        json: Optional[dict] = None,
        **kwargs: Any,
    ) -> Response:
        """
        This class represents a callable for an http or https request.
        :param url:
        :param method: http method
        :param kwargs:
        :return:
        """


# pylint: disable=unused-argument
async def async_request(
    url: str,
    method: str,
    headers: Optional[dict] = None,
    json: Optional[dict] = None,
    **kwargs: Any,
) -> Response:
    async with aiohttp.ClientSession() as session:
        async with session.request(
            method=method, url=url, headers=headers, json=json
        ) as resp:
            r = Response(
                status=resp.status,
                content=await resp.content.read(),
            )
            return r
