import streamlit as st  # type: ignore

def convert_units(value, unit_from, unit_to):  # type: ignore
    conversions = {
        "meter_kilometer": 0.001,   # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000,    # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001,     # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000       # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a unique key based on input and output units

# Logic to convert units.
    if key in conversions:
        conversion = conversions[key]
        return value * conversion  # Return correct value

    else: 
        return 'Conversion not supported'

# Streamlit UI
st.title("Unit Converter")

value = st.number_input("Enter your unit value:", min_value=0.0)
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert it!"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value is: {result}")  
