import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from duckduckgo_search import DDGS


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')


def gen_content(prompt):
    response = model.generate_content(prompt)
    print(f"[PROMPT]: {prompt}")
    print(f"[AI]: {response.text}")
    return response.text


class TravelPlanner:
    def __init__(self, travel_depart, travel_destination, travel_season, travel_duration,
                 travel_people, travel_style, travel_transport):
        self.travel_depart = travel_depart
        self.travel_destination = travel_destination
        self.travel_season = travel_season
        self.travel_duration = travel_duration
        self.travel_people = travel_people
        self.travel_style = travel_style
        self.travel_transport = travel_transport

    def generate_content(self):
        prompt = f'''
        You are an expert at planning trips.
        Your are good at finding sights, local food, excellent restaurants, and hotels.
        Use provided resources delimited by triple quotes to make recommendation. 
        
        """
        https://guide.michelin.com/en, https://www.lonelyplanet.com/, Trip advisor, Yelp, Expedia
        """
        The travel will at {self.travel_season} and the travel style is {self.travel_style}. 
        Step 1. Please estimate the round trip flights tickets price 
                from {self.travel_depart} to {self.travel_destination}. 
            
        Step 2. The trip at {self.travel_destination} will last {self.travel_duration} days and totally 
                {self.travel_people} people.
                Each day, please recommend at least one sight and three restaurants.
                You need to write a summary and score each sights and restaurants out of 10.
                Give a short summary or introduction of the sights, restaurants, and foods, also estimate the cost.
                Each day, Give the transport plan using {self.travel_transport} as main travel transport.
        Step 3: Find several hotels rates good and is convenient to go to all the place you mentioned above.
        Step 4. Estimate the cost of the trip using US Dollars.
        '''

        response = model.generate_content(prompt)
        return response.text

    def generate_sights(self):
        images = []
        prompt_start = f"Give me one of the famous sights at {self.travel_destination}"
        sights = [gen_content(prompt_start)]
        print("----------")
        for cnt in range(self.travel_duration):
            prompt = "\n".join(sights) + '\n' + f"Nice, can you tell me another one at {self.travel_destination}?"
            sights.append(gen_content(prompt))
            print("------------")
        for i in range(self.travel_duration):
            results = DDGS().images(
                keywords=sights[i],
                region="wt-wt",
                safesearch="off",
                size=None,
                color=None,
                type_image="photo",
                layout=None,
                license_image=None,
                max_results=1,
            )
            images.append(results)
        return sights, images


if '__main__' == __name__:
    st.title(" 🏖️Taste Trekker")
    st.subheader("Your Personal Travel Planner Good at Finding Local Food and Excellent Restaurants")

    # User Inputs
    depart = st.text_input("Enter your travel departure:")
    dest = st.text_input("Enter your travel destination:")
    season = st.selectbox("Select the travel season:", options=["Spring", "Summer", "Autumn", "Winter"])
    duration = st.slider("Choose the duration of the trip (days):", min_value=1, max_value=30)
    people = st.number_input("Enter the number of people traveling:", min_value=1, max_value=50)
    style = st.selectbox("Select the travel style:", options=["Romantic", "Fulfilling", "Relaxed", "Excited"])
    transport = st.selectbox("Choose your preferred transportation:",
                             options=["Car", "Public Transport", "Bicycle", "Plane"])

    if st.button("Generate Travel Plan"):
        plan = TravelPlanner(depart, dest, season, duration, people, style, transport)
        travel_sights, travel_images = plan.generate_sights()
        reply = plan.generate_content()
        st.write(reply)
        st.write("Here are some pictures from Duck Duck GO search engin:")
        for i in range(len(travel_sights) - 1):
            st.write(travel_sights[i])
            for img in travel_images[i]:
                st.image(img['image'])


