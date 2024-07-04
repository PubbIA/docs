import streamlit as st

def main():
    st.title('Simple Streamlit App')
    
    # Display a button
    if st.button('Click me!'):
        st.write('Button clicked!')

if __name__ == '__main__':
    main()
