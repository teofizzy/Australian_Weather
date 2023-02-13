import streamlit as st
import numpy as np
import pickle
import xgboost
import sklearn

# Loading the model
loaded_model = pickle.load(open('model.pkl', 'rb'))

# defining a predictive function
def predict_rain_tomorrow(Location, MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine,
                          WindGustDir, WindGustSpd, WindDir9am, WindDir3pm, WindSpd9am,
                          WindSpd3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm,
                          Cloud9am, Cloud3pm, Temp9am, Temp3pm, RainToday):
    
    # locations
    if Location == 'AliceSprings':
        Location = 0
    elif Location == 'Brisbane':
        Location = 1
    elif Location == 'Cairns':
        Location = 2
    elif Location == 'Canberra':
        Location = 3
    elif Location == 'Cobar':
        Location = 4
    elif Location == 'CoffsHarbour':
        Location = 5
    elif Location == 'Darwin':
        Location = 6
    elif Location == 'Hobart':
        Location = 7
    elif Location == 'Melbourne':
        Location = 8
    elif Location == 'MelbourneAirport':
        Location = 9
    elif Location == 'Mildura':
        Location = 10
    elif Location == 'Moree':
        Location = 11
    elif Location == 'MountGambier':
        Location = 12
    elif Location == 'NorfolkIsland':
        Location = 13
    elif Location == 'Nutrioopta':
        Location = 14
    elif Location == 'Perth':
        Location = 15
    elif Location == 'PerthAirport':
        Location = 16
    elif Location == 'Portland':
        Location = 17
    elif Location == 'Sale':
        Location = 18
    elif Location == 'Sydney':
        Location = 19
    elif Location == 'SydneyAirport':
        Location = 20
    elif Location == 'Townsville':
        Location = 21
    elif Location == 'WaggaWagga':
        Location = 22
    elif Location == 'Watsnoia':
        Location = 23
    elif Location == 'Williamtown':
        Location = 24
    elif Location == 'Woomera':
        Location = 25
    else:
        Location = 26
     
     # WindGustDir
        
    if WindGustDir == 'E':
        WindGustDir = 0
    elif WindGustDir == 'ENE':
        WindGustDir = 1
    elif WindGustDir == 'ESE':
        WindGustDir= 2
    elif WindGustDir == 'N':
        WindGustDir = 3
    elif WindGustDir == 'NE':
        WindGustDir = 4
    elif WindGustDir == 'NNE':
        WindGustDir = 5
    elif WindGustDir == 'NNW':
        WindGustDir = 6
    elif WindGustDir == 'NW':
        WindGustDir = 7
    elif WindGustDir == 'S':
        WindGustDir = 8
    elif WindGustDir == 'SE':
        WindGustDir = 9
    elif WindGustDir == 'SSE':
        WindGustDir = 10
    elif WindGustDir == 'SSW':
        WindGustDir= 11
    elif WindGustDir == 'SW':
        WindGustDir = 12
    elif WindGustDir == 'W':
        WindGustDir = 13
    elif WindGustDir == 'WNW':
        WindGustDir = 14
    elif WindGustDir == 'WSW':
        WindGustDir = 15
                    
    # WindDir9am
    
    if WindDir9am == 'E':
        WindDir9am = 0
    elif WindDir9am == 'ENE':
        WindDir9am = 1
    elif WindDir9am == 'ESE':
        WindDir9am= 2
    elif WindDir9am == 'N':
        WindDir9am = 3
    elif WindDir9am == 'NE':
        WindDir9am = 4
    elif WindDir9am == 'NNE':
        WindDir9am = 5
    elif WindDir9am == 'NNW':
        WindDir9am = 6
    elif WindDir9am == 'NW':
        WindDir9am = 7
    elif WindDir9am == 'S':
        WindDir9am = 8
    elif WindDir9am == 'SE':
        WindDir9am = 9
    elif WindDir9am == 'SSE':
        WindDir9am = 10
    elif WindDir9am == 'SSW':
        WindDir9am= 11
    elif WindDir9am == 'SW':
        WindDir9am = 12
    elif WindDir9am == 'W':
        WindDir9am = 13
    elif WindDir9am == 'WNW':
        WindDir9am = 14
    elif WindDir9am == 'WSW':
        WindDir9am = 15
    
    # WindDir3pm
       
    if WindDir3pm == 'E':
        WindDir3pm = 0
    elif WindDir3pm == 'ENE':
        WindDir3pm = 1
    elif WindDir3pm == 'ESE':
        WindDir3pm= 2
    elif WindDir3pm == 'N':
        WindDir3pm = 3
    elif WindDir3pm == 'NE':
        WindDir3pm = 4
    elif WindDir3pm == 'NNE':
        WindDir3pm = 5
    elif WindDir3pm == 'NNW':
        WindDir3pm = 6
    elif WindDir3pm == 'NW':
        WindDir3pm = 7
    elif WindDir3pm == 'S':
        WindDir3pm = 8
    elif WindDir3pm == 'SE':
        WindDir3pm = 9
    elif WindDir3pm == 'SSE':
        WindDir3pm = 10
    elif WindDir3pm == 'SSW':
        WindDir3pm= 11
    elif WindDir3pm == 'SW':
        WindDir3pm = 12
    elif WindDir3pm == 'W':
        WindDir3pm = 13
    elif WindDir3pm == 'WNW':
        WindDir3pm = 14
    elif WindDir3pm == 'WSW':
        WindDir3pm = 15
            
        
            
        # Rain Today
    if RainToday == 'No':
        RainToday = 0
    elif RainToday == 'Yes':
        RainToday = 1
     
     # Input the data       
    input_data = np.asarray([Location, MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine,
                          WindGustDir, WindGustSpd, WindDir9am, WindDir3pm, WindSpd9am,
                          WindSpd3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm,
                          Cloud9am, Cloud3pm, Temp9am, Temp3pm, RainToday])
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'It will not rain tomorrow'
    else:
        return 'It will rain tomorrow'

# Setting up the app
def main():
    st.title("Australian Weather Prediction app")
    
    # Location
    Location = st.selectbox("Location of interest (within Australia):", ['AliceSprings',
                                            'Brisbane',
                                            'Cairns',
                                            'Canberra',
                                            'Cobar',
                                            'CoffsHarbour',
                                            'Darwin',
                                            'Hobart',
                                            'Melbourne',
                                            'MelbourneAirport',
                                            'Mildura',
                                            'Moree',
                                            'MountGambier',
                                            'NorfolkIsland',
                                            'Nuriootpa',
                                            'Perth',
                                            'PerthAirport',
                                            'Portland',
                                            'Sale',
                                            'Sydney',
                                            'SydneyAirport',
                                            'Townsville',
                                            'WaggaWagga',
                                            'Watsonia',
                                            'Williamtown',
                                            'Woomera'])
    # MinTemp
    MinTemp = st.slider(label = "Slide to enter minimum temperature of a particular day (degree celcius)", 
                        min_value=-30, 
                        max_value=60)
    
    # MaxTemp
    MaxTemp = st.slider(label="Slide to enter maximum temperature of a particular day (degree celcius)", 
                        min_value=-30, 
                        max_value=60)
    
    # Rainfall
    Rainfall = st.slider(label = "Rainfall during a particular day (millimeters)", 
                         min_value=0, 
                         max_value=1000)
    
    # Evaporation
    Evaporation = st.slider(label = 'Evaporation during a particular day (millimeters)', 
                            min_value=0, 
                            max_value=1000)
    
    # Sunshine
    Sunshine = st.slider(label=" Bright sunshine during a particular day (hours)", 
                         min_value=0, 
                         max_value=24)
    
    #WindGustDir
    WindGustDir = st.selectbox(label='The direction of the strongest gust during a particular day (16 compass points):',
                               options=['E',
                                        'ENE',
                                        'ESE',
                                        'N',
                                        'NE',
                                        'NNE',
                                        'NNW',
                                        'NW',
                                        'S',
                                        'SE',
                                        'SSE',
                                        'SSW',
                                        'SW',
                                        'W',
                                        'WNW',
                                        'WSW'])
    # WindGustSpd
    WindGustSpd = st.slider(label='speed of the strongest gust during a particular day (km/hr)', min_value=0, max_value=500)
    
    # WindDir9am
    WindDir9am = st.selectbox(label='Direction of the wind for 10 minutes prior to 9 am on a particular day (16 compass points)',
                              options=['E',
                                        'ENE',
                                        'ESE',
                                        'N',
                                        'NE',
                                        'NNE',
                                        'NNW',
                                        'NW',
                                        'S',
                                        'SE',
                                        'SSE',
                                        'SSW',
                                        'SW',
                                        'W',
                                        'WNW',
                                        'WSW'])
    
    # WindDir3pm
    WindDir3pm = st.selectbox(label='Direction of the wind for 10 minutes prior to 3 pm on a particular day (16 compass points)',
                              options=['E',
                                        'ENE',
                                        'ESE',
                                        'N',
                                        'NE',
                                        'NNE',
                                        'NNW',
                                        'NW',
                                        'S',
                                        'SE',
                                        'SSE',
                                        'SSW',
                                        'SW',
                                        'W',
                                        'WNW',
                                        'WSW'])
    
    # WindSpd9am
    WindSpd9am = st.slider(label='The speed of the wind for 10 minutes prior to 9 am on a particular day (Km/hr)', 
                           min_value=0, 
                           max_value=500)
    
    # WindSpd3pm
    WindSpd3pm = st.slider(label='The speed of wind for 10 minutes prior to 3 pm on a particular day (km/hr)', 
                           min_value=0, 
                           max_value=500)
    
    # Humidity9am
    Humidity9am = st.slider(label='The humidity of the wind at 9 am (percent) on a particular day', 
                            min_value=0, 
                            max_value=100)
    
    # Humidity 3pm
    Humidity3pm = st.slider(label='The humidity of the wind at 3 pm (percent) on a particular day', 
                            min_value=0, 
                            max_value=100)
    
    # Pressure9am
    Pressure9am = st.slider(label='Atmospheric pressure at 9 am (in hectopascals) on a particular day', 
                            min_value=200, 
                            max_value=3000)
    
    # Pressure3pm
    Pressure3pm =st.slider(label='Atmospheric pressure at 3pm (in hectopascals) on a particular day', 
                           min_value=200, 
                           max_value=3000)
    
    #Cloud9am
    Cloud9am = st.slider(label='Cloud obscured portions of the sky at 9am on a particular day (eighths)', 
                         min_value=0, 
                         max_value=20)
    
    # Cloud3pm
    Cloud3pm =st.slider(label='Cloud obscured portions of the sky at 3pm on a particular day (eighths)',
                        min_value=0,
                        max_value=20)
    
    # Temp9am
    Temp9am = st.slider(label="The temperature at 9 am on a particular day (degrees celcius)",
                        min_value=-30,
                        max_value=70)
    
    Temp3pm = st.slider(label='The temperature at 3pm on a particular day (degrees celcius)',
                        min_value=-30,
                        max_value=70)
    
    # RainToday
    RainToday = st.selectbox(label='Did it rain today?',
                             options=['No', 'Yes'])    
    
    # Prediction
    Raintomorrow = ''
    
    if st.button("Will it rain tomorrow?"):
        Raintomorrow = predict_rain_tomorrow(Location, MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine,
                          WindGustDir, WindGustSpd, WindDir9am, WindDir3pm, WindSpd9am,
                          WindSpd3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm,
                          Cloud9am, Cloud3pm, Temp9am, Temp3pm, RainToday)
        
        if Raintomorrow == 'It will rain tomorrow':
            st.success(Raintomorrow)
            
        else:
            st.warning(Raintomorrow)
            
if __name__ == '__main__':
    main()
    