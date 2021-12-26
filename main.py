import asyncio
import argparse
import configparser

from typing import Literal, Type, Union
from nirvana.coalesce_api import RequestData, CoalesceApi
from nirvana.coalesce_stragety import AverageCoalesce, MinCoalesce, AbstractCoalesce
from nirvana.clients.request_client import async_request


async def main(config_filename: str, coalesce_strategy: Literal["min", "avg"]) -> None:
    config = configparser.ConfigParser()
    config.read(config_filename)

    urls = []

    for section in config.sections():
        request_data = RequestData(
            url=config[section]["url"], method=config[section]["method"]
        )
        urls.append(request_data)

    coalesce_factory: Union[Type[MinCoalesce], Type[AverageCoalesce]]
    if coalesce_strategy == "min":
        coalesce_factory = MinCoalesce
    elif coalesce_strategy == "avg":
        coalesce_factory = AverageCoalesce
    else:
        raise AttributeError(f"Invalid coalesce strategy: {coalesce_strategy}")

    api = CoalesceApi(
        request=async_request, coalesce_factory=coalesce_factory, urls=urls
    )

    for i in range(3):
        print(await api.search(i))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, help="Config file")
    parser.add_argument(
        "--coalesce-strategy",
        type=str,
        default="avg",
        help="Coalesce strategy: min, avg",
    )

    args = parser.parse_args()
    asyncio.run(main(args.config, args.coalesce_strategy))
