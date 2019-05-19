from UnleashClient.api import get_feature_toggles
from UnleashClient.loader import load_features
from UnleashClient.constants import FEATURES_URL
from UnleashClient.utils import LOGGER


def fetch_and_load_features(url,
                            app_name,
                            instance_id,
                            custom_headers,
                            cache,
                            features,
                            strategy_mapping):
    feature_provisioning = get_feature_toggles(url, app_name, instance_id, custom_headers)

    if feature_provisioning:
        cache[FEATURES_URL] = feature_provisioning
        cache.sync()
    else:
        LOGGER.info("Unable to get feature flag toggles, using cached values.")

    load_features(cache, features, strategy_mapping)
