from abc import ABC, abstractmethod
from typing import Collection, Union


class AbstractCoalesce(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    def _validate_data(self, data: dict[str, Union[float, int]]) -> None:
        """
        verify if the dict structure is valid: no missing key, no unknown keys
        :param data:
        :return:
        """
        for key, value in data.items():
            if not isinstance(key, str):
                raise AttributeError(f"Key is not str: {key} type: {type(key)}")
            if not isinstance(value, int) and not isinstance(value, float):
                raise AttributeError(f"Invalid value: {value} type: {type(value)}")

    @abstractmethod
    def get_keys(self) -> Collection[str]:
        """
        :return: the list of known keys
        """

    def add_data(self, data: dict[str, Union[float, int]]) -> None:
        """
        :param data: a dict
        """
        self._validate_data(data)
        self._add_data(data)

    @abstractmethod
    def _add_data(self, data: dict[str, Union[float, int]]) -> None:
        pass

    @abstractmethod
    def get_coalesced(self) -> dict[str, Union[float, int]]:
        """
        :return: the coalesced data
        """


class MinCoalesce(AbstractCoalesce):
    def __init__(self) -> None:
        super().__init__()
        self.d: dict[str, Union[float, int]] = {}

    def reset(self) -> None:
        self.d = {}

    def get_keys(self) -> Collection[str]:
        if self.d:
            return self.d.keys()
        else:
            return {}

    def _add_data(self, data: dict[str, Union[float, int]]) -> None:
        if not self.d:
            self.d = data
            return
        for key, value in data.items():
            if value < self.d[key]:
                self.d[key] = value

    def get_coalesced(self) -> dict[str, float]:
        return self.d


class AverageCoalesce(AbstractCoalesce):
    def __init__(self) -> None:
        super().__init__()
        self.d: dict[str, Union[float, int]] = {}
        self.n = 0

    def reset(self) -> None:
        self.d = {}
        self.n = 0

    def get_keys(self) -> Collection[str]:
        if self.d:
            return self.d.keys()
        else:
            return {}

    def _add_data(self, data: dict[str, Union[float, int]]) -> None:
        if self.d:
            for key, value in data.items():
                self.d[key] += value
        else:
            self.d = data
        self.n += 1

    def get_coalesced(self) -> dict[str, Union[float, int]]:
        return {key: value / self.n for key, value in self.d.items()}
