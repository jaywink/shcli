import pkg_resources

from shcli.api import create

__all__ = ("create",)


try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    __version__ = None
