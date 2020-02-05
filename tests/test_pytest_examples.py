from charger import __version__
from textwrap import dedent
import pytest


def test_version():
    assert __version__ == "0.6.0"


# @pytest.mark.xfail(reason="Demo of long string comparison")
def test_long_string():
    long_string_a = dedent(
        """
        Basic research is performed without thought of practical ends.
        It results in general knowledge and an understanding of nature and its laws.

        A worker in basic scientific research is motivated by a driving curiosity about the unknown.
        """
    )
    long_string_b = dedent(
        """
        Basic research is performed without ends of practical thoughts.
        It results in general knowledge and an understanding of nature and its laws.

        A worker in basic scientific research is motivated by a driving unknown about curiosity.
        """
    )
    assert long_string_a != long_string_b
