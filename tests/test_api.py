from nirvana.clients.request_client import RequestProtocol, Response
import pytest
from typing import Optional, Any
from nirvana.coalesce_stragety import MinCoalesce
from nirvana.coalesce_api import CoalesceApi, RequestData


@pytest.fixture
def request_fixture() -> RequestProtocol:
    async def async_request(
        url: str,
        method: str,
        headers: Optional[dict] = None,
        json: Optional[dict] = None,
        **kwargs: Any,
    ) -> Response:
        return Response(
            status=200, content=bytes('{"a": 1, "b": 2}\n', encoding="utf-8")
        )

    return async_request


@pytest.mark.asyncio
async def test(request_fixture: RequestProtocol) -> None:
    r = await request_fixture(url="a", method="get")
    assert r.status == 200


@pytest.mark.asyncio
async def test_api_should_work(request_fixture: RequestProtocol) -> None:
    api = CoalesceApi(
        request=request_fixture,
        coalesce_factory=MinCoalesce,
        urls=[RequestData(url="http://url/{member_id}", method="get")],
    )

    r = await api.search(1)
    assert r["a"] == 1
    assert r["b"] == 2
