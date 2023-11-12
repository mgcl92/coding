from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Index2DArrayIterator:
    matrix: list[list[int]]

    def __iter__(self) -> Iterator[int]:
        for row in self.matrix:
            yield from row

def index_2d_array_in_1d(array: list[list[int]], index: int) -> int:
    rows = len(array)
    cols = len(array[0])
    if rows == 0 or rows == 0:
        raise ValueError("No items in array!")

    if index < 0 or index >= rows * cols:
        raise ValueError("Index is out of range!")

    return array[index // cols][index % cols]