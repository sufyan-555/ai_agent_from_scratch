import streamlit as st
from agent import Agent
import os
from dotenv import load_dotenv
from tools import calculator

# Load environment variables
load_dotenv()
api = os.environ["hf_api"]

# Tool configuration
tools = {"calculator": calculator}

# Initialize the Agent
agent = Agent(token=api, tools=tools)

# Streamlit Page Configuration
st.set_page_config(page_title="Agent Chat Interface", layout="wide")

# Layout
col1, col2 = st.columns([2, 1], gap="large")

# Chat Section (Left Column)
with col1:
    st.markdown(
        """
        <h1 style="text-align: center; color: #4A90E2;">🤖 Agent Chat Interface</h1>
        <hr style="border: 1px solid #ddd;">
        """,
        unsafe_allow_html=True,
    )
    user_input = st.text_input("Chat with Agent",placeholder="Type your message here...")
    if user_input:
        if user_input.strip():
            response = agent.ask(query=user_input)
            st.markdown(
                f"""
                <div style="background-color: #E3F2FD; padding: 15px; margin-top: 20px; border-radius: 10px; border-left: 5px solid #4A90E2;">
                    Assistant:< {response}
                </div>
                """,
                unsafe_allow_html=True,
            )

# Verbose Logs Section (Right Column)
with col2:
    st.markdown(
        """
        <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px;">
            <h3 style="color: #4A90E2;">📋 Verbose Logs</h3>
            <p style="color: #666;">Details of the agent's internal processes appear here.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if agent.verbose_logs:
        for log in agent.verbose_logs:
            # Parse verbose log content
            if "Calling tool" in log:
                st.markdown(
                    f"""
                    <div style="background-color: #FFF3E0; padding: 10px; margin-top: 10px; border-radius: 10px; border-left: 5px solid #FF9800;">
                        <p>🔍 {log}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif "Args" in log:
                st.markdown(
                    f"""
                    <div style="background-color: #E3F2FD; padding: 10px; margin-top: 10px; border-radius: 10px; border-left: 5px solid #2196F3;">
                        <p>🛠️ {log}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif "Thought" in log:
                st.markdown(
                    f"""
                    <div style="background-color: #F3E5F5; padding: 10px; margin-top: 10px; border-radius: 10px; border-left: 5px solid #9C27B0;">
                        <p>💡 {log}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif "Tool Response" in log:
                st.markdown(
                    f"""
                    <div style="background-color: #E8F5E9; padding: 10px; margin-top: 10px; border-radius: 10px; border-left: 5px solid #4CAF50;">
                        <p>⚙️ {log}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                    <div style="background-color: #FAFAFA; padding: 10px; margin-top: 10px; border-radius: 10px; border-left: 5px solid #BDBDBD;">
                        <p>{log}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    else:
        st.markdown(
            """
            <div style="background-color: #FFEBEE; padding: 15px; margin-top: 10px; border-radius: 10px; border-left: 5px solid #F44336;">
                <p>No verbose logs available yet.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )