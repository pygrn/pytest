import hypothesis.strategies as st
import pytest
from hypothesis import given

from catchup.utils import gigabytes2bytes


@given(size_gigabytes=st.integers())
def test_gigabytes2bytes(size_gigabytes: int):
    if size_gigabytes < 0:
        with pytest.raises(Exception):
            gigabytes2bytes(size_gigabytes)
    else:
        gigabytes2bytes(size_gigabytes)
