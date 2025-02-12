VERSION = "1.0.0"

from .linstorapi import ApiCallResponse, ErrorReport
from .linstorapi import Linstor, MultiLinstor
from .resource import Resource, Volume
from .kv import KV
from .config import Config
from .responses import StoragePoolDriver
from .linstorapi import ResourceData
from .size_calc import SizeCalc
from .errors import LinstorError, LinstorTimeoutError, LinstorNetworkError, LinstorApiCallError, LinstorArgumentError
from .errors import LinstorReadOnlyAfterSetError
from . import sharedconsts as consts

try:
    from linstor.consts_githash import GITHASH
except ImportError:
    GITHASH = 'GIT-hash: UNKNOWN'
