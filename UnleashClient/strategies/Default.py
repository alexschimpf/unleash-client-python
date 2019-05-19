from UnleashClient.strategies import Strategy


class Default(Strategy):
    def __call__(self, context=None):
        """
        Return true if enabled.

        :return:
        """
        return True
