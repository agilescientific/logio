"""TotalDepth - a suite of Petrophysical software."""

__all__ = ['LAS', 'LIS', 'RP66', 'test', 'util',]


class ExceptionTotalDepth(Exception):
    """Specialisation of an exception class for TotalDepth package."""
    pass


__version__ = "unknown"
try:
        from ._version import __version__
except ImportError:
        pass

