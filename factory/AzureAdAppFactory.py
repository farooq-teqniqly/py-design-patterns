from msal import ConfidentialClientApplication


class AzureAdAppFactory:
    @classmethod
    def create(cls, **kwargs) -> ConfidentialClientApplication:
        client_id = kwargs["client_id"]
        client_secret = kwargs["client_secret"]
        authority = kwargs["authority"]

        return ConfidentialClientApplication(
            client_id,
            client_secret,
            authority)
