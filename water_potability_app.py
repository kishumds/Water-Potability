import pandas as pd
import streamlit as st
import pickle


def make_df(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    df = pd.DataFrame({'ph': ph,
                'Hardness': hardness,
                'Solids': solids,
                'Chloramines': chloramines,
                'Sulfate': sulfate,
                'Conductivity': conductivity,
                'Organic_carbon': organic_carbon,
                'Trihalomethanes': trihalomethanes,
                'Turbidity': turbidity},
                index=[0])
    return df


def load_model():
    return pickle.load(open('model.pkl', 'rb'))


def make_prediction(df, model):
    prediction = model.predict(df)
    if prediction[0] == 0:
        return st.success("Water is potable.")
    else:
        return st.error("Water is not potable.")


def make_output(df, model, submit):
    if submit:
        try:
            st.write('Result: ')
            make_prediction(df, model)
        except Exception as e:
            return st.error(str(e))
    pass


def main():
    html_temp = '''
    <div style="background-color:blue; padding:10px">
    <h2 style="color:white; text-align:center">Water Potability</h2>
    </div>
    '''

    st.markdown(html_temp, unsafe_allow_html=True)

    st.sidebar.title("About")
    st.sidebar.info("Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection. This app predicts whether water is potable or not from given measurement.")
    st.sidebar.write("")
    st.sidebar.write("Created by Kishan Modasiya.")
    
    st.info("Enter values and check whether water is potable.")


    ph = st.text_input("PH (0-14)")
    hardness = st.text_input("Hardness (50.0-300.0)")
    solids = st.text_input("Solids (400.0-60000.0)")
    chloramines = st.text_input("Chloromines (1.0-13.0)")
    sulfate = st.text_input("Sulfate (130.0-480.0)")
    conductivity = st.text_input("Conductivity (200.0-750.0)")
    organic_carbon = st.text_input("Organic Carbon (2.5-27.0)")
    trihalomethanes = st.text_input("Trihalomethanes (0.75-120.0)")
    turbidity = st.text_input("Turbidity (1.50-6.50)")

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        submit = st.button('Predict')

    # submit = st.button('Predict')

    df = make_df(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)
    model = load_model()
    if submit:
        make_output(df, model, submit)
            

if __name__ == "__main__":
    main()