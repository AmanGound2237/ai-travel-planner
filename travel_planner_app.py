import streamlit as st

def collect_user_input():
    st.title("AI Travel Planner 🌏")
    st.markdown("Plan your perfect trip with AI assistance.")

    destination = st.text_input("Where are you planning to go?")
    duration = st.number_input("How many days?", min_value=1, max_value=60, step=1)
    travel_dates = st.text_input("Enter your travel dates (e.g., 12th May to 18th May)")
    purpose = st.selectbox("Purpose of Travel", ["Leisure", "Business", "Adventure", "Family", "Romantic", "Cultural"])

    budget = st.selectbox("Budget Range", ["Low", "Medium", "High"])
    interests = st.multiselect("Your Interests", ["Food", "Nature", "Shopping", "Nightlife", "Culture", "History", "Adventure", "Relaxation"])
    dietary = st.text_input("Any dietary preferences? (e.g., vegetarian, vegan, none)")
    walking = st.selectbox("Comfort with walking", ["Low", "Moderate", "High"])
    stay_type = st.selectbox("Accommodation Preference", ["Luxury", "Budget", "Central location"])

    submit = st.button("Generate Itinerary")

    return submit, destination, duration, travel_dates, purpose, budget, interests, dietary, walking, stay_type

def generate_itinerary(destination, duration, travel_dates, purpose, budget, interests, dietary, walking, stay_type):
    # Simulated response; in actual deployment, this would connect to an AI agent or API
    return f"""
**Your {duration}-Day Itinerary for {destination}**

Travel Dates: {travel_dates}

**Day 1:** Arrival and local exploration.
**Day 2:** Visit top-rated cultural sites and enjoy local cuisine.
**Day 3:** Hidden gems aligned with your interest in {', '.join(interests)}.
**Day 4:** Relaxation or nature walk depending on walking preference.
**Day 5:** Shopping/local experience based on your {purpose.lower()} trip.
**Day 6:** Optional day trip or leisure time.
**Day 7:** Souvenir shopping and return.

All accommodations are selected based on your preference for {stay_type.lower()} and dietary consideration: {dietary}.
"""

# Streamlit app execution
submit, destination, duration, travel_dates, purpose, budget, interests, dietary, walking, stay_type = collect_user_input()

if submit:
    if destination and duration and travel_dates:
        itinerary = generate_itinerary(destination, duration, travel_dates, purpose, budget, interests, dietary, walking, stay_type)
        st.markdown(itinerary)
    else:
        st.warning("Please fill out all required fields to generate the itinerary.")
