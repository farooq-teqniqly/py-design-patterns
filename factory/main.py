import os
from dotenv import load_dotenv
from factory.AzureAdAppFactory import AzureAdAppFactory

load_dotenv()


def main():
    app = AzureAdAppFactory.create(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        authority=os.getenv("AUTHORITY"))

    scopes = [os.getenv("SCOPE")]
    result = app.acquire_token_silent(scopes, account=None)

    if not result:
        result = app.acquire_token_for_client(scopes=scopes)

    print(result)


if __name__ == "__main__":
    main()
