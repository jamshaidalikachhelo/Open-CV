import phonenumbers
from phonenumbers import geocoder
import streamlit as st
'''
# Set background image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://.jpg") center;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
) '''

# Title and description
st.title("Phone Number Location Finder")
st.markdown("Enter a phone number to find its location.")

# Phone number input
phone_input = st.text_input("Enter phone number (include country code, e.g., +123456789):")

if phone_input:
    try:
        phone_number = phonenumbers.parse(phone_input)

        # Extract country name
        country_name = geocoder.country_name_for_number(phone_number, "en")

        # Extract province name
        province_name = geocoder.description_for_number(phone_number, "en")

        # Display location information
        st.markdown("**Phone Number Location:**")
        st.write(f"**Country:** {country_name}")
        st.write(f"**Province:** {province_name}")

    except phonenumbers.phonenumberutil.NumberParseException:
        st.error("Invalid phone number format. Please enter a valid phone number.")
