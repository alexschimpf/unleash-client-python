import logging
import mmh3  # pylint: disable=import-error

LOGGER = logging.getLogger(__name__)


def normalized_hash(identifier,
                    activation_group):
    return mmh3.hash("{}:{}".format(activation_group, identifier), signed=False) % 100 + 1
