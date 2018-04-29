from torch import Tensor
from typing import Any, Union, Tuple, Iterator

def Variable(t : Tensor, requires_grad : bool = True) -> Tensor: ...

# class Variable:
#       data = ... # type: Tensor
#       def __init__(self, t : Tensor) -> None : ...
#       def size(self) -> Tensor : ...
#       def __getitem__(self, indices : Tuple[Union[slice, int], ...]) -> Any : ...
#       def __add__(self, other : int) -> Variable : ...
#       def __iter__(self) -> Iterator[Any] : ...
#       def __next__(self) -> Any: ...
#       def backward(self) -> None : ...
#       ...
