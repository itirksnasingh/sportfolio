"""Initial Streamlit landing page for Sportfolio.

The application is a scaffold. It deliberately does not claim that planned
modelling, evaluation, or deployment features are implemented.
"""
import streamlit as st

st.set_page_config(page_title="Sportfolio", page_icon="🧪", layout="wide")
st.title("Sportfolio")
st.caption("Computer-vision-based sports movement analysis")
st.warning("Development scaffold: core workflows are being implemented.")

st.subheader("Research question")
st.write("How reliably can a single-camera pose-estimation pipeline extract interpretable movement measurements for a selected exercise, and how do camera angle, lighting, and landmark visibility affect those measurements?")

st.subheader("Planned methodology")
for item in ["Video upload and frame sampling", "Pretrained pose estimation using MediaPipe", "Initial scope limited to one movement, such as a bodyweight squat", "2D joint-angle calculations from visible landmarks", "Landmark overlays and measurement traces over time", "Rule-based educational feedback with visibility/confidence indicators", "Controlled recordings and manually checked reference frames"]:
    st.write("• " + item)

st.subheader("Project status")
st.write("Scope defined · Implementation in progress · Evaluation pending · Deployment pending")
