import enum

from .message import MessageMeta
from .trans import Trans as _

default_errors = dict(
    ERROR=_('x_error'),
    NO_PERMISSION=_('x_no_permission'),
    INVALID_PARAMS=_('x_invalid_params'),
    INVALID_VALUE=_('x_invalid_value'),
    DUPLICATE_SUBMIT=_('x_duplicate_submit'),
    DUPLICATE_REQUEST=_('x_duplicate_request'),
    SAVE_FAILED=_('x_save_failed'),
)


class ErrorMeta(MessageMeta):
    @classmethod
    def _promise_messages(mcs, classdict):
        """修复类属性字典

        :param classdict: 类属性字典
        """
        MessageMeta._promise_messages(classdict)
        for attr_name, detail in list(default_errors.items()):
            classdict[attr_name] = detail


class Error(enum.Enum, metaclass=ErrorMeta):
    API_ERROR = _('api_get_error')
