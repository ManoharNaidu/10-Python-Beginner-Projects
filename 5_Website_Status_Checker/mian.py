import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict

def check_status(url: str) -> None:
    try:
        response: Response = requests.get(url)

        # Info
        status_code: int = response.status_code
        headers : CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get('Content-Type', 'unknown')
        server: str = headers.get('Server', 'unknown')
        response_time: float = response.elapsed.total_seconds()

        # print the results
        print("---------------------------")
        print(f"URL: {url}")
        print(f"Status Code: {status_code}")
        print(f"Content Type: {content_type}")
        print(f"Server: {server}")
        print(f"Response Time: {response_time} seconds")
        print("---------------------------")

    except RequestException as e:
        print(f"Error: {e}")


def main() -> None:
    urls: list[str] = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.linkedin.com",
        "https://www.github.com",
        "https://www.youtube.com",
        "https://www.instagram.com",
        "https://www.netflix.com",
        "https://www.spotify.com",
        "https://www.amazon.com",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.yahoo.com",
        "https://indently.io"
    ]

    for url in urls:
        check_status(url)

if __name__ == "__main__":
    main()