"""HWB class."""
from .. import hwb as base
from ...css import parse
from ...css import serialize
from ...types import Vector
from typing import Union, Optional, Tuple, Any, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from ...color import Color


class HWB(base.HWB):
    """HWB class."""

    def to_string(
        self,
        parent: 'Color',
        *,
        alpha: Optional[bool] = None,
        precision: Optional[int] = None,
        fit: Union[str, bool] = True,
        none: bool = False,
        **kwargs: Any
    ) -> str:
        """Convert to CSS."""

        return serialize.serialize_css(
            parent,
            func='hwb',
            alpha=alpha,
            precision=precision,
            fit=fit,
            none=none,
            color=kwargs.get('color', False)
        )

    @classmethod
    def match(
        cls,
        string: str,
        start: int = 0,
        fullmatch: bool = True
    ) -> Optional[Tuple[Tuple[Vector, float], int]]:
        """Match a CSS color string."""

        return parse.parse_css(cls, string, start, fullmatch)
