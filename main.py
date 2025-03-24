from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

api_key = os.environ.get("api_key")

# Initialize the model
def get_gemini_model():
    return ChatGoogleGenerativeAI(model='gemini-2.0-pro-exp-02-05', api_key=SecretStr(api_key))

async def scrape_play_store_html(review: str, app_id: str, scroll_timeout: int = 120) -> str:
    base_url = f"https://play.google.com/store/apps/details?id={app_id}&hl=en"

    # task = f"""
    # 1. Navigate to {base_url}.
    # 2. Click the 'See all reviews' button.
    # 3. Sort reviews by 'Newest'.
    # 4. Filter reviews by '{review}'.
    # 5. simulate a mouse scroll on the popup menu opened after clicking the see all reviews that is scrolable to load the dynamic content. for 120 seconds and return the HTML content.
    # """
    task = f"""Open the Google Play Store app page:

1.Navigate to {base_url} using a headless browser.
Ensure the page is fully loaded before interacting with elements.
Click the 'See all reviews' button:

2.Locate and click the 'See all reviews' button.
This opens a scrollable popup modal containing all user reviews.
Sort reviews by 'Newest':

3.Click on the sorting dropdown menu inside the popup.
Select 'Newest' to reorder reviews based on the latest submissions.
Wait for the popup to update with the sorted content.
Apply Star Rating Filter ('{review}'):

4.Open the filter menu inside the popup.
Locate and click on the 'Star rating' filter option.
Select the {review} rating (e.g., '2-star' reviews).
Wait for the popup to refresh and display only filtered reviews.
Simulate Scrolling Inside the Popup to Load More Reviews:

5.Identify the scrollable container inside the review popup.
Perform a smooth, incremental scroll within this popup to mimic human behavior.
Continue scrolling for 12 seconds (or until no new content loads).
Ensure that all dynamically loaded reviews are captured.
Extract and Return the Final HTML Content:

6.Once scrolling is complete, retrieve the entire HTML structure of the review section.
Ensure the captured content includes all visible reviews after filtering.
Return the extracted HTML for further processing.
"""

    llm = get_gemini_model()
    agent = Agent(
        task=task,
        llm=llm
    )

    history = await agent.run()
    
    # Extract HTML content from the last visited page
    page_content = history[-1].response.content if history else "No data retrieved"
    
    return page_content

if __name__ == "__main__":
    async def main():
        app_id = "com.muthootfincorpone.superapp"
        review = "2-star"
        result = await scrape_play_store_html(review, app_id)
        print(result)

    asyncio.run(main())
