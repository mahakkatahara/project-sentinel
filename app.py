import streamlit as st

st.set_page_config(page_title="Project Sentinel", page_icon="🛡️")

st.title("🛡️ Project Sentinel")
st.subheader("AI Agents That Supervise Other AI Agents")

query = st.text_area(
    "Enter your request:",
    "I want to buy a gaming laptop under ₹70,000 for college and coding."
)

if st.button("Analyze with Sentinel"):
    st.success("Sentinel analysis completed!")

    st.header("Planner Agent")
    st.write("Found 3 possible laptop options: Lenovo LOQ, HP Victus, Acer Nitro.")

    st.header("Risk Agent")
    st.write("Acer Nitro may have heating issues. HP Victus has average build quality. Lenovo LOQ has acceptable risk.")

    st.header("Finance Agent")
    st.write("Lenovo LOQ gives the best performance-to-price ratio under ₹70,000.")

    st.header("Policy Agent")
    st.write("All selected options satisfy the user's budget and usage requirements.")

    st.header("Audit Agent")
    st.write("""
    Final Recommendation: Lenovo LOQ
    
    Reason:
    - Within budget
    - Good for gaming and coding
    - Best value for money
    - Acceptable risk level
    
    Decision Status: Approved
    """)