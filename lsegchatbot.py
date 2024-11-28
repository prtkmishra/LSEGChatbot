"""
main.py
Author: Prateek Mishra
Description: 
            Streamlit server to enable chatbot interface
"""
############################################################################################################################################
import logging
import streamlit as st
from process_data import Processor

############################################################################################################################################

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("./log/lsegchatbot.log"),  # Log to a file
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

############################################################################################################################################

class chatbot:
    """
    Initialise Streamlit app and process the input prompts
    """
    def __init__(self):
        
        # Initialize Streamlit App
        st.title("LSEG Stock Chatbot")
        logger.info("Chatbot initialized")
        objProcessor = Processor() # Create processor object
        home_menu = objProcessor.home_menu() # Get the home menu
        # Initialize Home menu
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {'role': 'assistant', 'content': f'Hello! Welcome to LSEG. I am here to help you'},
                {'role': 'assistant', 'content': f'Please Select a Stock Exchange'},
                {'role': 'assistant', 'type': 'table', 'content': st.dataframe(home_menu, hide_index= True)},
                ]
        logger.info("Home menu loaded successfully")

        # Display chat message history
        for message in st.session_state.messages:
            with st.chat_message(message['role']):
                st.markdown(message['content'])

        # User Query
        if prompt := st.chat_input('Enter your query here....'):
            logger.info(f"User query received: {prompt}")
            stock_exchange = objProcessor.stock_exchange() # Get the list of stock exchanges
            st.session_state.messages.append({'role': 'user', 'type': 'text', 'content': prompt})
            
            # Markdown for user prompt
            with st.chat_message('user'):
                st.markdown(prompt)
            # Condition check for stock exchanges
            if any(prompt.strip() in x for x in stock_exchange):
                try:
                    stock_menu = objProcessor.show_stock_menu(prompt)
                    response = f"Which Stock Exchange would you like to check {st.dataframe(stock_menu['stockName'], hide_index= True)}"
                    st.session_state.messages.append({'role': 'assistant', 'content': response})
                    logger.info(f"Response sent to user: {response}")
                except Exception as e:
                    logger.error(f"Error processing user input: {e}", exc_info=True)
                    response = 'Please choose the correct option'
                    st.session_state.messages.append({'role': 'assistant', 'content': response})
            # Condition check for stock items
            elif any(prompt.strip() in x for x in objProcessor.stockmenu_df['stockName'].to_list()):
                try:
                    stock_values = objProcessor.stock_values(prompt)
                    response = f"{st.write(stock_values)}"
                    st.session_state.messages.append({'role': 'assistant', 'type': 'text', 'content': response})
                    logger.info(f"Response sent to user: {response}")
                except Exception as e:
                    logger.error(f"Error processing user input: {e}", exc_info=True)
                    response = 'Please choose the correct option'
                    st.session_state.messages.append({'role': 'assistant', 'content': response})
            # Condition check for home menu
            elif 'home' in prompt.lower().strip():
                try:
                    response = st.dataframe(home_menu, hide_index= True)
                    st.session_state.messages.append({'role': 'assistant', 'type': 'text', 'content': f'Home: {response}'})  
                    logger.info(f"Response sent to user: {response}")
                except Exception as e:
                    logger.error(f"Error processing user input: {e}", exc_info=True)
                    response = 'Please choose the correct option'
                    st.session_state.messages.append({'role': 'assistant', 'content': response})
            # Condition check for 'go back'
            elif 'go back' in prompt.lower().strip():
                try:
                    response = st.dataframe(objProcessor.stockmenu_df, hide_index= True)
                    st.session_state.messages.append({'role': 'assistant', 'type': 'text', 'content': response})
                    logger.info(f"Response sent to user: {response}")
                except Exception as e:
                    logger.error(f"Error processing user input: {e}", exc_info=True)
                    response = 'Please choose the correct option'
                    st.session_state.messages.append({'role': 'assistant', 'content': response})
            else:
                response = f"Please choose a valid input.\n1. Home\n2. Go Back"
                st.session_state.messages.append({'role': 'assistant', 'type': 'text', 'content': response})
                logger.info(f"Response sent to user: {response}")

if __name__ == '__main__':
    chatbot()
