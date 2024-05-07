# Pro Taste Trekker
## Overview
Your Personal Travel Planner Good at Finding Local Food and Excellent Restaurants and can generate picture of the food.
App webpage: https://510lab6-kghmbs7qx97ajza2b7kem6.streamlit.app/

- Prompt engineering learning: https://colab.research.google.com/drive/1RIXdTtdUxXTx2tNxSWrKKOOTwQP7qJ50?usp=sharing

Contains 2 parts:
- Generate template for AI's answer.(Prompt engineering)
- User input interface in web app.

## Getting Started
- Get an API key in Google
- Create a streamlit app using Gemini API
- Use prompts engineering skills to get more accurate answers

## Lessons Learned
1. Split the task in to multiple steps, use Multi-step prompts in this homework, the Gemini can provide higher quality travel plans.
2. Provide some travel website as reference, such as Michelin Guide, Lonely Planet, Trip advisor, Yelp, Expedia. Gemini needs to make recommendations based on above resource and give an overall rates to let user easier to choose.
3. Summarize the conversation, use a loop to get a list of famous sights as the answer from Gemini. Saving in a list can make “advanced search” possible.
4. Based on 3, using Duck Duck Go python search library to search the images for each sights saved in the list and show the images on the travel plan.

## Next step
- I try many ways but still can't get all the correct links, so that might be the next step.
- Sometimes will generate images with lo-quality. I may try to fix it. 