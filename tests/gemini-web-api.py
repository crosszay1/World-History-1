import asyncio
from gemini_webapi import GeminiClient

# Replace "COOKIE VALUE HERE" with your actual cookie values.
# Leave Secure_1PSIDTS empty if it's not available for your account.


async def main():
    # If browser-cookie3 is installed, simply use `client = GeminiClient()`
    client = GeminiClient()
    await client.init(timeout=30, auto_close=False, close_delay=300, auto_refresh=True)
    response = await client.generate_content("Hello World!")
    print(response.text)



asyncio.run(main())